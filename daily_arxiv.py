# -*- coding: utf-8 -*-
"""
daily_arxiv_new.py - 机器人/计算机视觉相关 arXiv 论文每日抓取与展示（重构版）

功能：
- 按 config 中的关键词从 arXiv 拉取最新论文，生成 README 与 GitHub Pages 用 Markdown
- 使用类架构，模块清晰，便于扩展
- JSON 存储为字典格式，包含摘要；每分类采用固定长度队列，满时淘汰最旧条目
"""

import os
import re
import json
import arxiv
import yaml
import logging
import argparse
import datetime
import subprocess
import requests
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

from gemini_api import batch_summarize_structured

# ---------------------------------------------------------------------------
# 日志与常量
# ---------------------------------------------------------------------------

logging.basicConfig(
    format='[%(asctime)s %(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.INFO
)

ARXIV_ABS_URL = "http://arxiv.org/abs/"

# 单条论文在 JSON 中的字段名（便于扩展与文档）
PAPER_FIELDS = (
    "paper_id", "title", "abstract", "authors_display",
    "pdf_url", "code_url", "date", "primary_category"
)




# ---------------------------------------------------------------------------
# 配置加载模块
# ---------------------------------------------------------------------------

class ConfigLoader:
    """
    负责从 YAML 加载配置，并将 keywords 下的 filters 转为 arXiv 查询串。
    接口：load(path) -> dict；不依赖全局路径，便于测试与扩展。
    """

    @staticmethod
    def _build_query(filters: List[str]) -> str:
        """将 filters 列表转为 arXiv 查询串，多词加双引号，用 OR 连接。"""
        parts = []
        for i, f in enumerate(filters):
            s = f'"{f}"' if len(f.split()) > 1 else f
            parts.append(s)
        return " OR ".join(parts)

    @classmethod
    def load(cls, config_path: str) -> dict:
        """
        加载配置文件并生成查询映射。
        :param config_path: 配置文件路径（如 config.yaml）
        :return: 包含原始配置及 'kv'（分类名 -> 查询串）的字典
        """
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        if not config:
            config = {}
        keywords_cfg = config.get('keywords', {})
        config['kv'] = {
            k: cls._build_query(v['filters'])
            for k, v in keywords_cfg.items()
        }
        logging.info("Config loaded: kv keys = %s", list(config.get('kv', {}).keys()))
        return config


# ---------------------------------------------------------------------------
# 论文抓取模块
# ---------------------------------------------------------------------------

class PaperFetcher:
    """
    从 arXiv 拉取论文元数据，返回结构化的论文字典列表。
    接口：fetch(topic, query, max_results) -> List[dict]
    """

    @staticmethod
    def _extract_code_url(comments: Optional[str]) -> Optional[str]:
        """从论文 comments 中提取第一个 http(s) 链接作为代码链接。"""
        if not comments:
            return None
        urls = re.findall(r'(https?://[^\s,;]+)', comments)
        return urls[0] if urls else None

    @classmethod
    def fetch(cls, topic: str, query: str, max_results: int = 20, gemini_api_key: str = None, batch_size: int = 10, gemini_model_id: str = 'gemini-2.5-flash') -> List[Dict[str, Any]]:
        """
        按查询从 arXiv 拉取论文，返回标准化的论文字典列表。
        :param topic: 分类名（如 Manipulation、VLA）
        :param query: arXiv 搜索串（已由 ConfigLoader 格式化）
        :param max_results: 该分类最多拉取篇数
        :return: [ { paper_id, title, abstract, authors_display, pdf_url, code_url, date, primary_category }, ... ]
        """
        papers = []
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        for result in search.results():
            paper_id = result.get_short_id()
            ver_pos = paper_id.find('v')
            paper_key = paper_id[:ver_pos] if ver_pos != -1 else paper_id
            pdf_url = ARXIV_ABS_URL + paper_key
            update_time = result.updated.date()
            authors = result.authors
            last_author = str(authors[-1]) if authors else ""
            code_url = cls._extract_code_url(result.comment)

            entry = {
                "paper_id": paper_key,
                "title": result.title,
                "abstract": (result.summary or "").replace("\n", " "),
                "authors_display": f"{last_author} Team",
                "pdf_url": pdf_url,
                "code_url": code_url,
                "date": str(update_time),
                "primary_category": getattr(result, 'primary_category', None) or "",
            }
            # add chinese summary
            # if gemini_api_key:
            #     entry["chinese_summary"] = summarize_with_gemini(entry["abstract"], gemini_api_key)
            # else:
            #     entry["chinese_summary"] = ""
            papers.append(entry)
            logging.info("Fetched: %s | %s | %s", update_time, result.title, last_author)
        
        if gemini_api_key:
            abstracts_list = [p["abstract"] for p in papers]
            summary_list = []
            for batch in range(0, len(abstracts_list), batch_size):
                batch_abstracts = abstracts_list[batch:batch+batch_size]
                batch_summaries = batch_summarize_structured(batch_abstracts, gemini_api_key, gemini_model_id)
                summary_list.extend(batch_summaries)
            for paper, summary in zip(papers, summary_list):
                paper["chinese_summary"] = summary.summary
            logging.info("Summarized %d papers with Gemini API", len(papers))
        else:
            logging.info("No Gemini API key provided, skipping summary generation")
        
        return papers


# ---------------------------------------------------------------------------
# 存储模块：固定长度队列 + 字典格式（含摘要）
# ---------------------------------------------------------------------------

class PaperStorage:
    """
    论文存储：JSON 为字典格式，每分类为固定长度队列，满时淘汰日期最旧的条目。
    接口：load(path) -> data; merge_and_trim(data, new_papers_by_topic, max_per_category) -> data; save(path, data)
    """

    META_KEY = "meta"
    CATEGORIES_KEY = "categories"
    META_UPDATED = "updated"
    META_MAX_PER_CATEGORY = "max_papers_per_category"

    @classmethod
    def load(cls, path: str) -> Dict[str, Any]:
        """
        从 JSON 文件加载数据。若文件不存在或为空，返回符合 schema 的空结构。
        若文件为旧版格式（无 meta/categories），则返回空结构，首次运行后将以新格式重写。
        Schema: { "meta": { "updated": str, "max_papers_per_category": int }, "categories": { topic: [ paper_dict, ... ] } }
        """
        empty = {
            cls.META_KEY: {cls.META_UPDATED: "", cls.META_MAX_PER_CATEGORY: 500},
            cls.CATEGORIES_KEY: {},
        }
        p = Path(path)
        if not p.exists() or p.stat().st_size == 0:
            return empty
        try:
            with open(path, 'r', encoding='utf-8') as f:
                raw = json.load(f)
        except (json.JSONDecodeError, OSError):
            return empty
        if not isinstance(raw, dict):
            return empty
        meta = raw.get(cls.META_KEY)
        if not isinstance(meta, dict):
            meta = {cls.META_UPDATED: "", cls.META_MAX_PER_CATEGORY: 500}
        categories = raw.get(cls.CATEGORIES_KEY)
        if not isinstance(categories, dict):
            categories = {}
        return {cls.META_KEY: meta, cls.CATEGORIES_KEY: categories}

    @classmethod
    def merge_and_trim(
        cls,
        data: Dict[str, Any],
        new_papers_by_topic: Dict[str, List[Dict[str, Any]]],
        max_per_category: int,
    ) -> Dict[str, Any]:
        """
        将新论文按分类合并进 data['categories']，每分类按日期降序后只保留前 max_per_category 条（队列淘汰最旧）。
        :param data: 现有存储数据（含 meta、categories）
        :param new_papers_by_topic: { topic: [ paper_dict, ... ] }
        :param max_per_category: 每分类最大保留条数
        :return: 合并并截断后的 data（原地修改并返回）
        """
        categories = data[cls.CATEGORIES_KEY]
        for topic, new_list in new_papers_by_topic.items():
            existing = categories.get(topic, [])
            by_id = {p["paper_id"]: p for p in existing}
            for p in new_list:
                by_id[p["paper_id"]] = p
            merged = list(by_id.values())
            merged.sort(key=lambda x: x.get("date", ""), reverse=True)
            categories[topic] = merged[:max_per_category]
        data[cls.META_KEY][cls.META_UPDATED] = str(datetime.date.today())
        data[cls.META_KEY][cls.META_MAX_PER_CATEGORY] = max_per_category
        return data

    @classmethod
    def save(cls, path: str, data: Dict[str, Any]) -> None:
        """将 data 写入 JSON 文件。"""
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Markdown 渲染模块
# ---------------------------------------------------------------------------

class MarkdownRenderer:
    """
    将存储数据渲染为 README 或 GitHub Pages 用 Markdown。
    接口：render(data, to_web, use_tc, show_badge, use_b2t) -> str
    """

    @staticmethod
    def _pretty_math(s: str) -> str:
        """对 $...$ 公式做简单格式化，避免渲染异常。"""
        match = re.search(r"\$.*\$", s)
        if match is None:
            return s
        start, end = match.span()
        trail = " " if s[:start][-1:] not in " *" else ""
        lead = " " if s[end:][:1] not in " *" else ""
        return s[:start] + trail + "$" + match.group()[1:-1].strip() + "$" + lead + s[end:]

    @staticmethod
    def _paper_to_table_row(paper: Dict[str, Any]) -> str:
        """将单条论文转为 README 表格一行（不含摘要）。"""
        d = paper.get("date", "")
        title = paper.get("title", "")
        authors = paper.get("authors_display", "")
        pid = paper.get("paper_id", "")
        pdf = paper.get("pdf_url", "")
        code = paper.get("code_url")
        chinese_summary = paper.get("chinese_summary", "")
        if code:
            return f"|**{d}**|**{title}**|{chinese_summary}|{authors}|[{pid}]({pdf})|**[link]({code})**|"
        return f"|**{d}**|**{title}**|{chinese_summary}|{authors}|[{pid}]({pdf})|null|"

    @classmethod
    def render(
        cls,
        data: Dict[str, Any],
        to_web: bool = False,
        use_tc: bool = True,
        use_b2t: bool = True,
    ) -> str:
        """
        将 PaperStorage 的 data 渲染成完整 Markdown 字符串。
        :param data: PaperStorage.load / merge_and_trim 后的数据
        :param to_web: 是否为 GitHub Pages（写 Jekyll layout、表格对齐）
        :param use_tc: 是否生成可折叠目录
        :param show_badge: 是否写 badge 链接
        :param use_b2t: 是否在每个分类后写 back to top
        """
        lines = []
        meta = data.get(PaperStorage.META_KEY, {})
        categories = data.get(PaperStorage.CATEGORIES_KEY, {})
        date_str = datetime.date.today().isoformat().replace('-', '.')

        if to_web:
            lines.append("---\nlayout: default\n---\n")

        # if show_badge:
        #     lines.append("[![Contributors][contributors-shield]][contributors-url]")
        #     lines.append("[![Forks][forks-shield]][forks-url]")
        #     lines.append("[![Stargazers][stars-shield]][stars-url]")
        #     lines.append("[![Issues][issues-shield]][issues-url]\n")

        lines.append("## Updated on " + date_str)
        # lines.append("> Usage instructions: [here](./docs/README.md#usage)\n")

        if use_tc and categories:
            lines.append("<details>")
            lines.append("  <summary>Table of Contents</summary>")
            lines.append("  <ol>")
            for kw in categories:
                if categories[kw]:
                    anchor = kw.replace(' ', '-').lower()
                    lines.append(f"    <li><a href=#{anchor}>{kw}</a></li>")
            lines.append("  </ol>")
            lines.append("</details>\n")

        for topic, papers in categories.items():
            if not papers:
                continue
            lines.append(f"## {topic}\n")
            if to_web:
                lines.append("| Publish Date | Title | Chinese Summary | Authors | PDF | Code |")
                lines.append("|:---------|:-----------------------|:------------------------|:---------|:------|:------|")
            else:
                lines.append("|Publish Date|Title|Chinese Summary|Authors|PDF|Code|")
                lines.append("|---|---|---|---|---|---|")
            # 已按日期降序存储，直接顺序输出
            for p in papers:
                lines.append(cls._pretty_math(cls._paper_to_table_row(p)))
            lines.append("")
            if use_b2t:
                top = "#updated-on-" + date_str.replace('.', '').replace(' ', '-').lower()
                lines.append(f"<p align=right>(<a href={top}>back to top</a>)</p>\n")

        # if show_badge:
        #     lines.append("[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge")
        #     lines.append("[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors")
        #     lines.append("[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge")
        #     lines.append("[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members")
        #     lines.append("[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge")
        #     lines.append("[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers")
        #     lines.append("[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge")
        #     lines.append("[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues\n")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# 主应用类：编排配置、抓取、存储、渲染
# ---------------------------------------------------------------------------

class ArxivDailyApp:
    """
    主应用：加载配置、抓取论文、合并队列存储、渲染 README 与 GitPage。
    扩展点：可子类化并重写 _fetch_all、_after_merge、_after_render 等以接入新功能。
    """

    def __init__(self, config_path: str = "config.yaml"):
        """
        :param config_path: 配置文件路径
        """
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self._storage_data: Optional[Dict[str, Any]] = None  # 当前加载的存储数据，可供扩展使用

    def load_config(self) -> Dict[str, Any]:
        """加载配置并返回。"""
        self.config = ConfigLoader.load(self.config_path)
        # 优先从环境变量中读取 GEMINI_API_KEY（例如 GitHub Actions Secrets），避免在仓库中明文存储
        env_key = os.getenv("GEMINI_API_KEY")
        if env_key:
            self.config["gemini_api_key"] = env_key
        return self.config

    def _fetch_all(self) -> Dict[str, List[Dict[str, Any]]]:
        """按 config 中 kv 抓取所有分类的论文。"""
        kv = self.config.get('kv', {})
        max_results = int(self.config.get('max_results', 20))
        result = {}
        for topic, query in kv.items():
            logging.info("Keyword: %s", topic)
            result[topic] = PaperFetcher.fetch(topic, query, max_results=max_results, 
                gemini_api_key=self.config.get('gemini_api_key', None), 
                batch_size=self.config.get('batch_size', 10), 
                gemini_model_id=self.config.get('gemini_model_id', 'gemini-2.5-flash'))
        return result

    def _get_max_papers_per_category(self) -> int:
        """每分类队列最大长度，默认 500。"""
        return int(self.config.get('max_papers_per_category', 500))

    def run(self) -> None:
        """
        主流程：抓取新论文并合并；然后从同一份 JSON 渲染 README 与 GitPage。
        data 数据格式：{ 
            "meta": { "updated": str, "max_papers_per_category": int }, 
            "categories": { topic: [ paper_dict, ... ] } 
        }
        """
        self.load_config()
        json_data_path = self.config.get('json_data_path', './docs/arxiv-daily.json')
        md_readme_path = self.config.get('md_readme_path', 'README.md')
        md_gitpage_path = self.config.get('md_gitpage_path', './docs/index.md')
        max_per_category = self._get_max_papers_per_category()

        data = PaperStorage.load(json_data_path)
        new_by_topic = self._fetch_all()
        data = PaperStorage.merge_and_trim(data, new_by_topic, max_per_category)
        PaperStorage.save(json_data_path, data)
        self._storage_data = data

        if self.config.get('publish_readme', True):
            md = MarkdownRenderer.render(data, to_web=False, use_tc=True, use_b2t=True)
            Path(md_readme_path).write_text(md, encoding='utf-8')
            logging.info("Update Readme finished")

        if self.config.get('publish_gitpage', True):
            md_web = MarkdownRenderer.render(
                data, to_web=True, use_tc=False, use_b2t=False
            )
            Path(md_gitpage_path).write_text(md_web, encoding='utf-8')
            logging.info("Update GitPage finished")

    def get_storage_data(self) -> Optional[Dict[str, Any]]:
        """返回最近一次 run 使用的存储数据，便于扩展（如导出、统计）。"""
        return self._storage_data


# ---------------------------------------------------------------------------
# 命令行入口
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="arXiv 论文每日抓取与 README/GitPage 更新")
    parser.add_argument('--config_path', type=str, default='config.yaml', help='配置文件路径')

    args = parser.parse_args()

    app = ArxivDailyApp(config_path=args.config_path)
    app.run()

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Github Action Automatic Update Arxiv Daily Papers"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("Git commands executed successfully.")
    except subprocess.CalledProcessError:
        pass


if __name__ == "__main__":
    main()
