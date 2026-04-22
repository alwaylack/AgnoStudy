from pathlib import Path

from agno.db.sqlite import SqliteDb

from models import OpenAIModel


def run_sessions_history_example() -> None:
    """演示如何用 Session 和 History 实现多轮对话。"""
    # History 依赖数据库来保存消息记录，这里继续使用最轻量的 SQLite。
    db_path = Path("tmp/sessions.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno History Agent",
        db=SqliteDb(db_file=str(db_path)),
        # 开启后，Agno 会自动把最近几轮历史消息加入上下文。
        add_history_to_context=True,
        # 这里只取最近 3 轮，方便观察“带历史”和“不带历史”的区别。
        num_history_runs=3,
        instructions=[
            "你是 Agno 学习助手。",
            "请根据当前会话中的历史消息，保持回答前后一致。",
        ],
        markdown=True,
    )

    user_id = "student@example.com"
    session_id = "history_demo_session"

    print("\n--- 第 1 轮：建立上下文 ---")
    agent.print_response(
        "我正在学习 Agno，我更喜欢先看最小可运行示例。",
        user_id=user_id,
        session_id=session_id,
    )

    print("\n--- 第 2 轮：继续同一个 Session ---")
    agent.print_response(
        "请基于我刚才的偏好，给我一个学习建议。",
        user_id=user_id,
        session_id=session_id,
    )

    print("\n--- 第 3 轮：验证 Agent 是否能读取会话历史 ---")
    agent.print_response(
        "你还记得我喜欢什么样的学习方式吗？",
        user_id=user_id,
        session_id=session_id,
    )


if __name__ == "__main__":
    run_sessions_history_example()
