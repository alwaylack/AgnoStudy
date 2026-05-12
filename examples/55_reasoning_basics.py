"""Reasoning 基础示例。

演示 Agno 的 Reasoning 能力，包括：
1. 打开 reasoning=True
2. 控制 reasoning_min_steps / reasoning_max_steps
3. 观察 reasoning_content / reasoning_steps
4. 区分普通回答和显式推理流程
"""

from models import OpenAIModel


def print_reasoning_summary(response) -> None:
    """打印 reasoning 相关字段，便于观察。"""
    print("\n--- 响应内容 ---")
    print(response.content)

    print("\n--- reasoning_content ---")
    print(response.reasoning_content or "（当前模型/运行未返回 reasoning_content）")

    steps = response.reasoning_steps or []
    print(f"\n--- reasoning_steps 数量: {len(steps)} ---")
    for index, step in enumerate(steps, 1):
        print(f"{index}. {step}")


def run_reasoning_basics_example() -> None:
    """演示 Agno 的 Reasoning 基础能力。"""
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Reasoning Agent",
        reasoning=True,
        reasoning_min_steps=1,
        reasoning_max_steps=4,
        instructions=[
            "你是 Agno Reasoning 示例的学习助教。",
            "请先分析问题，再给出简洁结论。",
        ],
        markdown=True,
        debug_mode=True,
    )

    response = agent.run(
        "我已经学完 Dependency Injection、Hooks。请判断 Skills、Reasoning、Multimodal 哪个更适合作为下一组重点，并给出理由。",
        user_id="student@example.com",
        session_id="lesson_55_reasoning_demo",
    )
    print_reasoning_summary(response)

    print("\n--- 关键观察点 ---")
    print("1. reasoning=True 会让 Agent 使用显式推理流程。")
    print("2. reasoning_min_steps / reasoning_max_steps 控制推理步数范围。")
    print("3. response.reasoning_content 和 response.reasoning_steps 可用于观察推理产物。")
    print("4. 适合复杂规划、比较、诊断类任务；简单问答不一定需要。")


if __name__ == "__main__":
    run_reasoning_basics_example()
