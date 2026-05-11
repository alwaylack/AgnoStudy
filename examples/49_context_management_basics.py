"""Context Management 基础示例。

演示 Agno 的上下文管理能力，包括：
1. 基于 Agno 内置功能的历史消息控制
2. 多轮工具调用场景下的上下文清理
3. 长对话场景下的上下文压缩
"""

from pathlib import Path

from agno.db.sqlite import SqliteDb

from models import OpenAIModel


# ---------------------------------------------------------------------------
# 辅助函数：模拟工具调用
# ---------------------------------------------------------------------------

def search_topic(topic: str) -> str:
    """模拟搜索工具，返回关于主题的信息。"""
    results = {
        "agent": "Agent 是 AI 应用的核心组件，负责处理输入、调用工具、生成输出。",
        "memory": "Memory 用于存储长期记忆，跨会话保持用户偏好和历史信息。",
        "tools": "Tools 是 Agent 可以调用的函数，扩展 Agent 的能力边界。",
        "workflow": "Workflow 用于编排多个 Agent 和工具，实现复杂的业务流程。",
    }
    return results.get(topic.lower(), f"关于 {topic} 的搜索结果：这是一个重要的 Agno 概念。")


def analyze_content(content: str) -> str:
    """模拟分析工具，对内容进行分析。"""
    return f"分析结果：'{content[:50]}...' 包含关键信息，建议深入学习。"


def generate_summary(text: str) -> str:
    """模拟总结工具，生成简洁摘要。"""
    return f"摘要：{text[:30]}... 的核心要点已提取完成。"


def get_learning_path(stage: str) -> str:
    """模拟学习路径工具，返回推荐的学习路径。"""
    paths = {
        "beginner": "建议从 Agent 基础开始，逐步学习 Tools、Memory、Knowledge。",
        "intermediate": "建议深入学习 Team、Workflow、Runtime 等高级特性。",
        "advanced": "建议关注生产化：Guardrails、Evals、Tracing、Human in the Loop。",
    }
    return paths.get(stage.lower(), f"根据 {stage} 阶段，推荐定制化学习路径。")


# ---------------------------------------------------------------------------
# 辅助函数：输出上下文快照
# ---------------------------------------------------------------------------

def print_context_snapshot(
    messages: list,
    label: str = "当前上下文",
) -> None:
    """输出当前上下文的状态，帮助观察消息数量和内容。"""
    print(f"\n--- {label} ---")
    print(f"消息总数: {len(messages)}")

    if not messages:
        print("（无消息）")
        return

    # 统计消息类型
    role_counts = {}
    for msg in messages:
        role = msg.role if hasattr(msg, 'role') else 'unknown'
        role_counts[role] = role_counts.get(role, 0) + 1

    print(f"消息类型分布: {role_counts}")

    # 显示最后一条消息预览
    last_msg = messages[-1]
    content = last_msg.content if hasattr(last_msg, 'content') else str(last_msg)
    print(f"最后一条消息预览: {str(content)[:80]}...")


def print_token_metrics(response, label: str = "Token 消耗") -> None:
    """输出 token 消耗指标，帮助对比上下文管理效果。"""
    print(f"\n--- {label} ---")
    if response and hasattr(response, 'metrics') and response.metrics:
        metrics = response.metrics
        if hasattr(metrics, 'input_tokens'):
            print(f"Input tokens: {metrics.input_tokens:,}")
        if hasattr(metrics, 'output_tokens'):
            print(f"Output tokens: {metrics.output_tokens:,}")
        if hasattr(metrics, 'total_tokens'):
            print(f"Total tokens: {metrics.total_tokens:,}")
    else:
        print("（无法获取 token 指标）")


# ---------------------------------------------------------------------------
# 场景一：多轮工具调用清理
# ---------------------------------------------------------------------------

def run_tool_call_cleanup_demo(
    model: OpenAIModel,
    db: SqliteDb,
) -> None:
    """演示多轮工具调用场景下的上下文清理策略。"""
    print("\n" + "=" * 60)
    print("场景一：多轮工具调用清理")
    print("=" * 60)

    agent = model.create_agent(
        name="Tool Cleanup Agent",
        db=db,
        tools=[search_topic, analyze_content, generate_summary],
        instructions=[
            "你是 Agno 学习助手，可以帮助用户搜索和分析学习资料。",
            "当用户询问关于 Agno 概念的问题时，请调用搜索工具获取信息。",
            "如果需要分析内容，请调用分析工具。",
            "如果需要总结，请调用总结工具。",
        ],
        add_history_to_context=True,
        num_history_runs=3,
        markdown=True,
    )

    user_id = "student@example.com"
    session_id = "lesson_49_tool_cleanup_demo"

    # 模拟多轮工具调用
    print("\n--- 第 1 轮：搜索 Agent 概念 ---")
    response1 = agent.run(
        "请帮我搜索一下什么是 Agent。",
        user_id=user_id,
        session_id=session_id,
    )
    print(response1.content)
    print_token_metrics(response1, "第 1 轮 Token 消耗")

    print("\n--- 第 2 轮：搜索 Memory 概念 ---")
    response2 = agent.run(
        "请帮我搜索一下什么是 Memory。",
        user_id=user_id,
        session_id=session_id,
    )
    print(response2.content)
    print_token_metrics(response2, "第 2 轮 Token 消耗")

    print("\n--- 第 3 轮：搜索 Tools 概念 ---")
    response3 = agent.run(
        "请帮我搜索一下什么是 Tools。",
        user_id=user_id,
        session_id=session_id,
    )
    print(response3.content)
    print_token_metrics(response3, "第 3 轮 Token 消耗")

    print("\n--- 第 4 轮：分析之前的内容 ---")
    response4 = agent.run(
        "请帮我分析一下之前搜索的三个概念（Agent、Memory、Tools）之间的关系。",
        user_id=user_id,
        session_id=session_id,
    )
    print(response4.content)
    print_token_metrics(response4, "第 4 轮 Token 消耗")

    print("\n--- 第 5 轮：生成总结 ---")
    response5 = agent.run(
        "请帮我总结一下今天学习的 Agno 核心概念。",
        user_id=user_id,
        session_id=session_id,
    )
    print(response5.content)
    print_token_metrics(response5, "第 5 轮 Token 消耗")

    # 展示上下文管理效果
    messages = agent.get_session_messages(
        session_id=session_id,
        last_n_runs=10,
    )
    print_context_snapshot(messages, "工具调用清理后的上下文")


# ---------------------------------------------------------------------------
# 场景二：长对话压缩
# ---------------------------------------------------------------------------

def run_conversation_compression_demo(
    model: OpenAIModel,
    db: SqliteDb,
) -> None:
    """演示长对话场景下的上下文压缩策略。"""
    print("\n" + "=" * 60)
    print("场景二：长对话压缩")
    print("=" * 60)

    # 使用较小的 num_history_runs 来模拟压缩效果
    agent = model.create_agent(
        name="Compression Agent",
        db=db,
        tools=[get_learning_path],
        instructions=[
            "你是 Agno 学习助手，可以帮助用户规划学习路径。",
            "请保持回答简洁，避免重复之前已经说过的内容。",
            "如果用户询问之前讨论过的内容，请基于当前上下文回答。",
        ],
        add_history_to_context=True,
        num_history_runs=2,  # 只保留最近 2 轮，模拟压缩效果
        markdown=True,
    )

    user_id = "student@example.com"
    session_id = "lesson_49_compression_demo"

    # 模拟长对话
    conversations = [
        "我刚开始学习 Agno，应该从哪里开始？",
        "我已经学完了 Agent 基础，下一步学什么？",
        "Tools 和 Memory 哪个更重要？",
        "我想学习多智能体协作，有什么建议？",
        "Team 和 Workflow 有什么区别？",
        "Runtime 是做什么的？",
        "我想把 Agent 部署到生产环境，需要学什么？",
        "Guardrails 和 Evals 是什么？",
        "Human in the Loop 怎么实现？",
        "Tracing 和监控怎么做？",
        "我之前问的第一个问题是什么？",  # 测试压缩后的记忆能力
    ]

    for i, message in enumerate(conversations, 1):
        print(f"\n--- 第 {i} 轮对话 ---")
        print(f"用户: {message}")
        response = agent.run(
            message,
            user_id=user_id,
            session_id=session_id,
        )
        print(f"助手: {response.content}")
        print_token_metrics(response, f"第 {i} 轮 Token 消耗")

    # 展示压缩后的上下文
    messages = agent.get_session_messages(
        session_id=session_id,
        last_n_runs=20,
    )
    print_context_snapshot(messages, "长对话压缩后的完整历史")

    # 展示注入到上下文的消息
    recent_messages = agent.get_session_messages(
        session_id=session_id,
        last_n_runs=2,
    )
    print_context_snapshot(recent_messages, "注入到上下文的最近消息（压缩效果）")


# ---------------------------------------------------------------------------
# 主函数
# ---------------------------------------------------------------------------

def run_context_management_basics_example() -> None:
    """演示 Agno 的 Context Management 基础能力。"""
    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "lesson_49_context_management.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # 创建数据库，使用单独的 session_table 便于观察
    db = SqliteDb(
        db_file=str(db_path),
        session_table="lesson_49_agent_sessions",
    )

    model = OpenAIModel.from_env()

    # 场景一：多轮工具调用清理
    run_tool_call_cleanup_demo(model=model, db=db)

    # 场景二：长对话压缩
    run_conversation_compression_demo(model=model, db=db)

    print("\n" + "=" * 60)
    print("Context Management 基础示例完成")
    print("=" * 60)
    print(f"\n数据库文件路径: {db_path}")
    print("\n关键观察点：")
    print("1. num_history_runs 控制注入到上下文的历史轮次")
    print("2. 较小的 num_history_runs 可以模拟上下文压缩效果")
    print("3. 工具调用结果也会占用上下文空间")
    print("4. 合理的上下文管理可以降低 token 消耗")


if __name__ == "__main__":
    run_context_management_basics_example()
