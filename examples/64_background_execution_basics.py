"""Background Execution 基础示例。

演示 Agno 的 Background Execution 能力，包括：
1. 使用 agent.arun(..., background=True)
2. 立即得到 pending run output
3. 理解后台运行和 stream 不能混用
4. 理解 background=True 必须配置数据库持久化
"""

import asyncio
import sys
from pathlib import Path

from agno.db.sqlite import SqliteDb

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models import OpenAIModel


async def run_background_execution_demo() -> None:
    """异步演示后台执行。"""
    db_path = PROJECT_ROOT / "tmp" / "lesson_64_background_execution.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Background execution 会先返回 pending run，再通过数据库持久化 run 状态。
    # 因此 Agno 要求 Agent 必须配置 db，否则会抛出 ValueError。
    db = SqliteDb(db_file=str(db_path))

    model = OpenAIModel.from_env()
    agent = model.create_agent(
        name="Background Execution Agent",
        db=db,
        instructions=[
            "你是 Background Execution 示例助教。",
            "请简洁说明后台运行适合什么任务。",
        ],
        markdown=True,
    )

    pending_output = await agent.arun(
        "请用 3 点说明 Agno background=True 的用途。",
        user_id="student@example.com",
        session_id="lesson_64_background_execution_demo",
        background=True,
        stream=False,
    )

    print("\n--- 后台运行返回值 ---")
    print(f"run_id: {pending_output.run_id}")
    print(f"status: {pending_output.status}")
    print(f"content: {pending_output.content}")

    print("\n--- 数据库配置 ---")
    print(f"db_path: {db_path}")


def run_background_execution_basics_example() -> None:
    """演示 Agno 的 Background Execution 基础能力。"""
    asyncio.run(run_background_execution_demo())

    print("\n--- 关键观察点 ---")
    print("1. agent.arun(..., background=True) 会立即返回 pending 运行对象。")
    print("2. 后台任务适合长时间执行、API 请求快速返回、异步工作流。")
    print("3. background=True 不能和 stream=True 混用。")
    print("4. background=True 必须给 Agent 配置数据库，用于保存和查询后台 run 状态。")


if __name__ == "__main__":
    run_background_execution_basics_example()
