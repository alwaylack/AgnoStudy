from models import OpenAIModel


def run_openai_compatible_example() -> None:
    """演示如何用 OpenAILike 接入兼容 OpenAI 的第三方模型。"""
    # 这里依然复用我们自己的模型封装类，避免每个示例都重复写配置代码。
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="OpenAI 兼容 Agent",
        instructions=[
            "你的回答需要简洁明了，帮助用户专注学习 Agno。"
        ],
        markdown=True,
    )

    agent.print_response("给我制定一个今天的 Agno 学习小计划。")


if __name__ == "__main__":
    run_openai_compatible_example()
