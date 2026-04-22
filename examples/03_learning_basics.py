from pathlib import Path

from agno.db.sqlite import SqliteDb

from models import OpenAIModel


def run_learning_basics_example() -> None:
    """演示官方文档中最基础的学习能力用法。"""
    # 学习能力需要一个数据库来保存用户信息，这里先用最轻量的 SQLite。
    db_path = Path("tmp/agents.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model = OpenAIModel.from_env()

    # 按照官方 Quickstart，直接把 learning 设为 True 即可开启基础学习能力。
    # 这样 Agent 会自动提取用户画像和用户记忆，并在后续会话中回忆起来。
    agent = model.create_agent(
        name="Agno Learning Agent",
        db=SqliteDb(db_file=str(db_path)),
        learning=True,
        markdown=True,
    )

    user_id = "student@example.com"

    print("\n--- 会话 1：告诉 Agent 你的偏好 ---")
    agent.print_response(
        "你好，我更喜欢带代码示例的解释，而且我正在学习 Agno。",
        user_id=user_id,
        session_id="session_1",
    )

    print("\n--- 会话 2：让 Agent 回忆它学到了什么 ---")
    agent.print_response(
        "你还记得我的学习偏好吗？",
        user_id=user_id,
        session_id="session_2",
    )


if __name__ == "__main__":
    run_learning_basics_example()
