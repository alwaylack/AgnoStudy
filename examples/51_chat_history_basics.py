from pathlib import Path

from agno.db.sqlite import SqliteDb

from models import OpenAIModel


def print_chat_history(agent, session_id: str, label: str) -> None:
    """读取并打印指定 session 的聊天历史。"""
    chat_history = agent.get_chat_history(session_id=session_id, last_n_runs=3)
    session_messages = agent.get_session_messages(session_id=session_id, last_n_runs=3)

    print(f"\n--- {label} ---")
    print(f"get_chat_history() 读取到的消息数量: {len(chat_history)}")
    print(f"get_session_messages() 读取到的消息数量: {len(session_messages)}")

    if not chat_history:
        print("当前还没有可读取的聊天历史。")
        return

    for index, message in enumerate(chat_history[-4:], 1):
        content = str(message.content).replace("\n", " ")
        print(f"{index}. {message.role}: {content[:120]}")


def run_chat_history_basics_example() -> None:
    """演示 Agno 的 Chat History 基础能力。"""
    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "lesson_51_chat_history.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model = OpenAIModel.from_env()
    db = SqliteDb(
        db_file=str(db_path),
        session_table="lesson_51_agent_sessions",
    )

    agent = model.create_agent(
        name="Agno Chat History Agent",
        db=db,
        add_history_to_context=True,
        num_history_runs=2,
        read_chat_history=True,
        search_session_history=True,
        num_history_sessions=3,
        store_history_messages=True,
        instructions=[
            "你是 Agno Chat History 示例的学习助教。",
            "回答要简洁，并尽量说明你是否基于当前会话历史或过去 session 做了判断。",
        ],
        markdown=True,
    )

    user_id = "student@example.com"
    main_session_id = "lesson_51_main_chat_history"
    review_session_id = "lesson_51_review_chat_history"

    print("\n--- 场景一：同一个 session 内自动注入最近历史 ---")
    first_response = agent.run(
        "我现在开始学习 Chat History。请记住：我喜欢用最小示例理解概念。",
        user_id=user_id,
        session_id=main_session_id,
    )
    print(first_response.content)

    second_response = agent.run(
        "请基于我的偏好，解释 Chat History 和 Session Management 的区别。",
        user_id=user_id,
        session_id=main_session_id,
    )
    print(second_response.content)

    print_chat_history(agent, main_session_id, "当前 session 的聊天历史")

    print("\n--- 场景二：创建另一个 session，给跨 session 搜索准备材料 ---")
    review_response = agent.run(
        "这是复习 session：我已经完成了 Database、Session Management、Context Management 和 State Management。",
        user_id=user_id,
        session_id=review_session_id,
    )
    print(review_response.content)

    print("\n--- 场景三：让 Agent 按需读取聊天历史 ---")
    history_response = agent.run(
        "请读取聊天历史，告诉我刚才提到的学习偏好是什么。",
        user_id=user_id,
        session_id=main_session_id,
    )
    print(history_response.content)

    print("\n--- 场景四：让 Agent 搜索过去 session 历史 ---")
    search_response = agent.run(
        "请根据过去的 session 历史，判断我最近已经学过哪些 Agno 主题。",
        user_id=user_id,
        session_id="lesson_51_search_chat_history",
    )
    print(search_response.content)

    print("\n--- 场景五：程序化读取最后一次运行结果 ---")
    last_run_output = agent.get_last_run_output(session_id=main_session_id)
    if last_run_output is None:
        print("没有读取到最后一次运行结果。")
    else:
        print(str(last_run_output.content)[:300])

    print("\n--- 数据库文件路径 ---")
    print(db_path)


if __name__ == "__main__":
    run_chat_history_basics_example()
