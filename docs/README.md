<p align="center">
  <h2 align="center"><br><ins>Robotics-arXiv-daily</ins><br>使用 GitHub Actions 自动更新机器人相关 arXiv 论文</h2>
</p>

## 简介

本仓库提供一套简单的脚本与工作流，用于：

- **按关键词从 arXiv 拉取机器人 / 操作 / Robot Learning 等论文**；
- **将结果写入 `docs/arxiv-daily.json` 并渲染为 `README.md` 与 `docs/index.md`**；
- 依托 **GitHub Actions**，实现 **每天自动更新**，可选开启 GitHub Pages 作为在线阅读页面。

## 代码结构概览

- **`daily_arxiv.py`**：主入口脚本，按 `config.yaml` 配置抓取论文、更新 JSON 和 Markdown。
- **`config.yaml`**：配置文件（关键词、最大论文数、文件路径、是否发布到 README / GitHub Pages 等）。
- **`gemini_api.py`**：调用 Gemini API，对论文摘要进行 **批量中文总结**（可选，若未配置 API Key 则自动跳过）。
- **`docs/arxiv-daily.json`**：论文数据存储文件（按分类存储，包含摘要/中文总结等信息）。
- **`docs/index.md`**：GitHub Pages 用的渲染结果页面。
- **`.github/workflows/daily-arxiv.yml`**：GitHub Actions 工作流（定时/手动触发）。

## 本地运行

- **安装依赖**

```bash
pip install -r requirements.txt
```

- **配置 `config.yaml`（至少确认以下字段）**
  - **`user_name`**：你的 GitHub 用户名。
  - **`repo_name`**：你的仓库名（例如 `robotics-arxiv-daily`）。
  - **`keywords`**：你感兴趣的主题（默认只包含 `Manipulation`，可以自行增加）。

- **（可选）配置 Gemini API Key**
  - 推荐通过环境变量传入：在本机设置 `GEMINI_API_KEY`，脚本会自动优先使用该值。
  - 若不配置，脚本会跳过中文摘要生成，但不影响其它流程。

- **运行脚本**

```bash
python daily_arxiv.py --config_path config.yaml
```

运行结束后，你会看到：

- 根目录下的 `README.md` 更新；
- `docs/index.md` 和 `docs/arxiv-daily.json` 更新。

## 使用 GitHub Actions 自动更新

### 1. Fork 仓库并修改配置

- **Fork 本仓库**到你自己的 GitHub 账号下。
- 修改 `config.yaml` 中的：
  - **`user_name`**：改成你的 GitHub 用户名；
  - **`repo_name`**：改成你的仓库名；
  - 按需调整 `max_results`、`max_papers_per_category`、`keywords` 等。

### 2. 配置 Gemini API Key（可选但推荐）

1. 打开 GitHub 仓库页面，进入：
   - `Settings` → `Secrets and variables` → `Actions` → `New repository secret`
2. 新建一个 Secret：
   - **Name**: `GEMINI_API_KEY`
   - **Value**: 你的真实 Gemini API Key
3. 工作流 `daily-arxiv.yml` 已经将此 Secret 注入为环境变量，`daily_arxiv.py` 会自动读取：
   - 有 Key：生成中文摘要；
   - 无 Key：跳过摘要生成。

### 3. 配置 GitHub Actions 权限与工作流

- **开启读写权限**
  - 进入仓库 `Settings` → `Actions` → `General` → `Workflow permissions`
  - 勾选 **`Read and write permissions`** 并保存。
- **启用工作流**
  - 到仓库的 `Actions` 页面；
  - 选择左侧的 `Daily arXiv Update`（来自 `.github/workflows/daily-arxiv.yml`）；
  - 按提示启用工作流，并可点击 `Run workflow` 手动运行一次。

> 工作流会：检出代码 → 安装依赖 → 运行 `daily_arxiv.py` → 使用脚本内置的 `git add/commit/push` 将变更推回仓库。

### 4. 配置 GitHub Pages（可选）

1. 打开仓库 `Settings` → `Pages`
2. 在 **Build and deployment** 中选择：
   - **Source**: `Deploy from a branch`
   - **Branch**: 选择 `main` 分支 和 `/docs` 目录
3. 保存后，GitHub 会自动部署 Pages。

部署完成后，你可以访问：

- `https://your_github_username.github.io/robotics-arxiv-daily`

页面内容来自 `docs/index.md`，由脚本自动更新。

## 自定义关键词与分类

- 在 `config.yaml` 的 `keywords` 字段下新增或修改分类，例如：

```yaml
keywords:
  "Manipulation":
    filters: ["Robot Manipulation", "Robotic Manipulation", "Robot Learning", "Imitation Learning"]
  "VLA":
    filters: ["Vision Language Action","Vision-Language-Action"]
  "Humanoid":
    filters: ["Humanoid Robot", "Humanoid"]
```

- 修改后：
  - 本地运行脚本，或
  - 推送到远程后，在 GitHub Actions 页面手动 `Run workflow`。

## 注意事项

- **分支名称**：`daily_arxiv.py` 中默认使用 `main` 分支做 `git push`，如果你的默认分支是 `master` 或其他名称，需要同步修改脚本中对应参数。
- **API 限额**：当 Gemini API 达到限额或被限流时，`gemini_api.py` 会返回空结果，不会中断主流程，只是对应论文的中文摘要字段为空。
- **隐私与安全**：请不要在 `config.yaml` 中写入真实的 API Key，始终通过 GitHub Secrets 或本地环境变量传入。 
