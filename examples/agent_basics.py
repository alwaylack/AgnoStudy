from models import OpenAIModel


def run_basic_example() -> None:
    """项目中的第一个 Agno 入门示例。"""
    # 先从环境变量中读取模型配置，保持示例代码足够简单。
    model = OpenAIModel.from_env()

    # 创建一个最基础的 Agent。
    agent = model.create_agent(
        name="Agno Beginner Agent",
        instructions=[
            "你正在一步一步指导初学者学习 Python 和 Agno。"
        ],
        markdown=True,
    )

    # 通过 print_response() 直接打印结果，这是官方文档里最常见的入门方式。
    agent.print_response("请用通俗易懂的语言解释 Agno 中的 Agent 是什么。")


if __name__ == "__main__":
    run_basic_example()
