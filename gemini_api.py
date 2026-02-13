from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

# 1. 定义单个摘要的结构
class PaperSummary(BaseModel):
    id: int = Field(description="The index ID of the input abstract, ensuring the order matches.")
    summary: str = Field(description="对摘要的中文总结，要求: 1. 简洁明了, 用几句话概括; 2. 保持严谨性和学术性; 3. 按照问题背景-方法思路-实验结果的逻辑介绍。")

# 2. 定义批量返回的容器结构 (关键步骤)
class SummaryBatch(BaseModel):
    summaries: List[PaperSummary] = Field(description="A list of summaries for the provided abstracts.")

def batch_summarize_structured(abstracts_list: List[str], api_key: str, model_id: str = "gemini-1.5-flash"):
    """
    使用 google-genai SDK 和 Pydantic 进行批量结构化总结。
    """
    if not abstracts_list:
        return []

    client = genai.Client(api_key=api_key)

    # 3. 构建 Prompt，明确输入数据的索引
    # 我们给每个摘要打上标号，让模型在返回时填写对应的 id
    input_text = ""
    for idx, text in enumerate(abstracts_list):
        input_text += f"\n--- Abstract ID: {idx} ---\n{text}\n"

    prompt = f"""
    You are an expert academic assistant. Please summarize the following academic abstracts into Chinese.
    
    Requirements:
    1. 简洁明了, 用几句话概括; 2. 保持严谨性和学术性; 3. 按照问题背景-方法思路-实验结果的逻辑介绍。
    4. Ensure the 'id' in the output matches the 'Abstract ID' provided in the input.
    
    Input Abstracts:
    {input_text}
    """

    try:
        # 4. 调用 API，直接传入 Pydantic 的 Schema
        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                # 这里直接传入 Pydantic 生成的 schema
                response_schema=SummaryBatch.model_json_schema(),
            )
        )
        
        # 5. 自动验证并转换为对象
        # response.text 是纯 JSON 字符串，validate_json 会自动将其映射为 SummaryBatch 对象
        batch_result = SummaryBatch.model_validate_json(response.text)
        
        # 按 ID 排序，防止模型乱序返回
        sorted_summaries = sorted(batch_result.summaries, key=lambda x: x.id)
        
        return sorted_summaries

    except Exception as e:
        # 当达到配额 / 速率限制等情况时，Gemini 通常会返回包含 quota / exceeded / 429 等关键词的错误信息
        err_msg = str(e).lower()
        if ("quota" in err_msg) or ("exceeded" in err_msg) or ("resource exhausted" in err_msg) or ("429" in err_msg):
            # 明确地在配额耗尽时返回空列表，让上层逻辑跳过摘要
            print("Gemini API quota reached or rate limited, returning empty summaries.")
            return []

        # 其他异常也保持原有行为：打印错误并返回空列表
        print(f"Error during API call or validation: {e}")
        return []

# --- 使用示例 ---
if __name__ == "__main__":
    # 填入你的 API Key
    MY_KEY = "YOUR_GEMINI_API_KEY"

    # 模拟两篇论文摘要
    abstracts = [
        # Abstract 0
        """
        Deep learning has achieved remarkable success in various fields. However, its application 
        to scientific discovery remains challenging due to the lack of interpretability. 
        In this paper, we propose WeakPDE-Net for discovering partial differential equations. 
        Experiments show it outperforms baselines in accuracy.
        """,
        # Abstract 1
        """
        Robotic reinforcement learning is often sample inefficient. We introduce PolyFlow, 
        a generative flow matching model for safe trajectory generation. 
        Tested on Unitree Go2 robots, our method achieves 99% success rate in locomotion tasks.
        """
    ]

    print(f"正在处理 {len(abstracts)} 篇摘要...\n")
    
    # 调用函数
    results = batch_summarize_structured(abstracts, MY_KEY)

    # 打印结果
    for summary in results:
        print(f"=== 论文 {summary.id}: {summary.summary} ===")