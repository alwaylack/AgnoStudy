from models import OpenAIModel


def run_builtin_tools_example() -> None:
    """演示如何注册并使用 Agno 内置的 DuckDuckGo 工具。"""
    try:
        from agno.tools.duckduckgo import DuckDuckGoTools
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装 DuckDuckGo 依赖：`uv pip install -U ddgs`"
        ) from exc

    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Builtin Tools Agent",
        # 这里注册的是 Agno 自带的 Toolkit，而不是我们自己写的函数。
        tools=[DuckDuckGoTools(enable_search=True, enable_news=False)],
        instructions=[
            "你是 Agno 学习助手。",
            "当问题需要联网搜索时，优先使用 DuckDuckGo 工具。",
            "请根据搜索结果给出简洁总结。",
        ],
        markdown=True,
        # 你当前的 agno 版本里可用这个参数观察工具执行过程。
        debug_mode=True,
    )

    agent.print_response("请搜索 Agno 官方文档里对 tools 的定义，并做一个简短总结。")


if __name__ == "__main__":
    run_builtin_tools_example()
