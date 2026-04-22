from models import OpenAIModel


def get_study_tip(topic: str) -> str:
    """根据主题返回一条固定的学习建议。"""
    tips = {
        "agent": "先理解 Agent 的输入、模型和输出，再继续学习工具和记忆。",
        "memory": "先区分 user_id 和 session_id，再观察 Agent 会记住什么。",
        "tools": "先从简单函数开始，把工具调用流程跑通，再接第三方服务。",
    }
    return tips.get(topic.lower(), f"先从最小示例开始学习 {topic}，逐步增加复杂度。")


def add_numbers(a: int, b: int) -> int:
    """演示最简单的计算工具。"""
    return a + b


def run_tools_basics_example() -> None:
    """演示如何给 Agno Agent 添加最基础的 Python 工具。"""
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Tools Agent",
        tools=[get_study_tip, add_numbers],
        instructions=[
            "你是 Agno 学习助手。",
            "当用户的问题适合调用工具时，优先调用工具。",
            "如果使用了工具，请结合工具结果给出简洁解释。",
        ],
        markdown=True,
        # 你当前安装的 agno 版本不支持 show_tool_calls，这里改用 debug_mode 观察执行过程。
        debug_mode=True,
    )

    print("\n--- 示例 1：让 Agent 调用学习建议工具 ---")
    agent.print_response("我正在学习 Agno 的 tools，给我一条学习建议。")

    print("\n--- 示例 2：让 Agent 调用计算工具 ---")
    agent.print_response("请帮我计算 13 + 29，并顺便告诉我这展示了什么工具能力。")


if __name__ == "__main__":
    run_tools_basics_example()
