from pathlib import Path

from agno.db.sqlite import SqliteDb

from models import OpenAIModel


def print_session_management_snapshot(agent, session_id: str) -> None:
    """输出当前 session 的管理信息，帮助观察 session 管理能力。"""
    session_name = agent.get_session_name(session_id=session_id)
    session_state = agent.get_session_state(session_id=session_id)
    session_messages = agent.get_session_messages(
        session_id=session_id,
        last_n_runs=2,
    )
    session_record = agent.get_session(session_id=session_id)

    print("\n--- Session 管理快照 ---")
    print(f"session_name: {session_name}")
    print(f"session_state: {session_state}")
    print(f"最近读取到的消息数量: {len(session_messages)}")

    if session_record is not None:
        print(f"session_id: {session_record.session_id}")
        print(f"保存的运行次数: {len(session_record.runs or [])}")

    if session_messages:
        print("\n--- 最近一条消息预览 ---")
        last_message = session_messages[-1]
        print(f"role: {last_message.role}")
        print(f"content: {str(last_message.content)[:120]}")


def run_session_management_basics_example() -> None:
    """演示 Agno 的 Session Management 基础能力。"""
    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "lesson_48_session_management.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model = OpenAIModel.from_env()
    agent = model.create_agent(
        name="Agno Session Management Agent",
        db=SqliteDb(db_file=str(db_path)),
        add_history_to_context=True,
        num_history_runs=2,
        instructions=[
            "你是 Agno Session Management 示例的学习助教。",
            "请根据当前会话上下文给出简洁、连续的回答。",
        ],
        markdown=True,
    )

    user_id = "student@example.com"
    session_id = "lesson_48_session_management_demo"

    print("\n--- 第 1 次运行：建立 session ---")
    first_response = agent.run(
        "我已经学完了 Input & Output 和 Database，现在准备学习 Session Management。",
        user_id=user_id,
        session_id=session_id,
    )
    print(first_response.content)

    # 这一课重点不只是“自动保存”，而是主动管理 session 本身。
    # 这里手动给 session 命名，并写入一些我们自己维护的状态。
    agent.set_session_name(
        session_id=session_id,
        session_name="Agno Session Management 学习记录",
    )
    agent.update_session_state(
        session_state_updates={
            "completed_lessons": ["46_input_output_basics", "47_database_basics"],
            "current_focus": "Session Management",
            "preferred_style": "最小可运行示例",
        },
        session_id=session_id,
    )

    print("\n--- 第 2 次运行：继续复用同一个 session，并读取刚才写入的状态 ---")
    second_response = agent.run(
        "请结合我当前这个 session 的学习重点，告诉我这一课最值得关注哪三个点。",
        user_id=user_id,
        session_id=session_id,
        add_session_state_to_context=True,
    )
    print(second_response.content)

    print_session_management_snapshot(agent=agent, session_id=session_id)
    print("\n--- 数据库文件路径 ---")
    print(db_path)


if __name__ == "__main__":
    run_session_management_basics_example()
