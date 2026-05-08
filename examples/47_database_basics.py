from pathlib import Path

from agno.db.base import SessionType
from agno.db.sqlite import SqliteDb

from models import OpenAIModel


def print_database_snapshot(db: SqliteDb, session_id: str, user_id: str) -> None:
    """读取当前数据库里的 Session 记录，帮助观察数据是否真的持久化。"""
    saved_session = db.get_session(
        session_id=session_id,
        session_type=SessionType.AGENT,
        user_id=user_id,
    )
    all_sessions = db.get_sessions(
        session_type=SessionType.AGENT,
        user_id=user_id,
        limit=20,
    )

    print("\n--- 数据库快照 ---")
    print(f"当前用户的 Agent Session 数量: {len(all_sessions)}")

    if saved_session is None:
        print("没有读取到当前 session 的持久化记录。")
        return

    print(f"session_id: {saved_session.session_id}")
    print(f"user_id: {saved_session.user_id}")
    print(f"保存的运行次数: {len(saved_session.runs or [])}")
    print(f"metadata: {saved_session.metadata or {}}")
    print(f"agent_data 键: {list((saved_session.agent_data or {}).keys())}")
    print(f"session_data 键: {list((saved_session.session_data or {}).keys())}")


def run_database_basics_example() -> None:
    """演示 Agno 的 Database 基础能力。"""
    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "lesson_47_database.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # 这一课显式创建数据库对象，方便你把“数据库能力”单独拎出来理解。
    # session_table 也单独命名，方便后续你自己在 SQLite 里排查和观察。
    db = SqliteDb(
        db_file=str(db_path),
        session_table="lesson_47_agent_sessions",
    )

    model = OpenAIModel.from_env()
    agent = model.create_agent(
        name="Agno Database Agent",
        db=db,
        metadata={"course": "47_database_basics"},
        add_history_to_context=True,
        num_history_runs=2,
        instructions=[
            "你是 Agno 数据库存储示例的学习助教。",
            "请保持回答简洁，并尽量体现出连续对话的上下文延续。",
        ],
        markdown=True,
    )

    user_id = "student@example.com"
    session_id = "lesson_47_database_demo"

    print("\n--- 第 1 次运行：写入第一条 session 记录 ---")
    first_response = agent.run(
        "我已经学到了 Input & Output，下一步准备学习 Database。",
        user_id=user_id,
        session_id=session_id,
        metadata={"run_stage": "first"},
    )
    print(first_response.content)

    print("\n--- 第 2 次运行：继续复用同一个 session_id ---")
    second_response = agent.run(
        "请基于我刚才的进度，告诉我这节 Database 课最该关注什么。",
        user_id=user_id,
        session_id=session_id,
        metadata={"run_stage": "second"},
    )
    print(second_response.content)

    print_database_snapshot(db=db, session_id=session_id, user_id=user_id)
    print("\n--- 数据库文件路径 ---")
    print(db_path)


if __name__ == "__main__":
    run_database_basics_example()
