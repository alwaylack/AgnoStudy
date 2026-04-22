from pathlib import Path

from agno.db.sqlite import SqliteDb
from agno.learn import LearningMachine, LearningMode, SessionContextConfig, UserMemoryConfig

from models import OpenAIModel


def run_learning_machine_memory_example() -> None:
    """演示如何使用 LearningMachine 精细配置学习能力。"""
    # LearningMachine 同样需要数据库保存学习结果，这里继续使用 SQLite。
    db_path = Path("tmp/learning_machine.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db = SqliteDb(db_file=str(db_path))

    model = OpenAIModel.from_env()

    # 和 learning=True 不同，这里把学习能力拆开配置：
    # 1. user_memory：长期记住用户偏好
    # 2. session_context：学习当前会话中的上下文事实
    learning = LearningMachine(
        db=db,
        user_memory=UserMemoryConfig(mode=LearningMode.ALWAYS),
        session_context=SessionContextConfig(mode=LearningMode.ALWAYS),
        debug_mode=True,
    )

    agent = model.create_agent(
        name="Agno LearningMachine Agent",
        db=db,
        learning=learning,
        instructions=[
            "你是 Agno 学习助手。",
            "请根据长期用户记忆和当前会话上下文来回答问题。",
        ],
        markdown=True,
    )

    user_id = "student@example.com"

    print("\n--- 会话 1：建立长期用户记忆 ---")
    agent.print_response(
        "我学习 Agno 时更喜欢先看最小示例，再看原理解释。",
        user_id=user_id,
        session_id="learning_machine_session_1",
    )

    print("\n--- 会话 2：让 Agent 回忆长期偏好 ---")
    agent.print_response(
        "你记得我的学习偏好吗？",
        user_id=user_id,
        session_id="learning_machine_session_2",
    )

    print("\n--- 会话 3：写入当前会话上下文 ---")
    agent.print_response(
        "我今天正在学习 Agno 的 LearningMachine，目标是理解 user_memory 和 session_context 的区别。",
        user_id=user_id,
        session_id="learning_machine_session_3",
    )

    print("\n--- 会话 4：验证当前会话上下文是否可用 ---")
    agent.print_response(
        "我今天这节课的重点是什么？",
        user_id=user_id,
        session_id="learning_machine_session_3",
    )


if __name__ == "__main__":
    run_learning_machine_memory_example()
