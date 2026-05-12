"""Context Compression 基础示例。

演示 Agno 的 Context Compression 能力，包括：
1. 使用 CompressionManager 配置工具结果压缩
2. 在 Agent 上启用 compress_tool_results
3. 通过阈值控制何时压缩工具结果
4. 说明压缩需要可用的压缩模型
"""

from agno.compression import CompressionManager

from models import OpenAIModel


def return_long_learning_notes(topic: str) -> str:
    """返回较长的学习笔记，用来触发工具结果压缩。"""
    paragraph = (
        f"{topic} 是 Agno 长上下文管理中的一部分。"
        "当工具调用返回大量文本时，直接把完整结果塞回上下文会增加 token 压力。"
        "压缩工具结果的目标是在保留决策所需事实的同时减少上下文占用。"
    )
    return "\n".join([paragraph for _ in range(8)])


def run_context_compression_basics_example() -> None:
    """演示 Agno 的 Context Compression 基础能力。"""
    model = OpenAIModel.from_env()
    compression_manager = CompressionManager(
        model=model.get_model(),
        compress_tool_results=True,
        compress_tool_results_limit=1,
    )

    agent = model.create_agent(
        name="Context Compression Agent",
        tools=[return_long_learning_notes],
        compress_tool_results=True,
        compression_manager=compression_manager,
        instructions=[
            "你是 Context Compression 示例助教。",
            "请调用工具获取笔记，然后总结压缩工具结果的价值。",
        ],
        markdown=True,
        debug_mode=True,
    )

    response = agent.run(
        "请获取 Context Compression 的学习笔记，并总结成 3 点。",
        user_id="student@example.com",
        session_id="lesson_62_context_compression_demo",
    )
    print("\n--- Agent 响应 ---")
    print(response.content)

    print("\n--- CompressionManager 配置 ---")
    print(f"compress_tool_results: {compression_manager.compress_tool_results}")
    print(f"compress_tool_results_limit: {compression_manager.compress_tool_results_limit}")
    print(f"stats: {compression_manager.stats}")

    print("\n--- 关键观察点 ---")
    print("1. compress_tool_results=True 会让 Agent 尝试压缩工具结果。")
    print("2. CompressionManager 决定压缩阈值、压缩模型和统计信息。")
    print("3. 适合工具返回大段文本、网页内容或检索结果的场景。")
    print("4. 这是上下文管理的生产化补充，不是普通摘要提示词的替代品。")


if __name__ == "__main__":
    run_context_compression_basics_example()
