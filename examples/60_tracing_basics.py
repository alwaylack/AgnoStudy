"""Tracing 基础示例。

演示 Agno 的 Tracing 能力，包括：
1. 用 SqliteDb 准备 trace 存储
2. 调用 setup_tracing 开启 OpenTelemetry instrumentation
3. 运行 Agent 后自动记录 spans
4. 处理本地缺少 OpenTelemetry 依赖的情况
"""

from pathlib import Path

from agno.db.sqlite import SqliteDb

from models import OpenAIModel


def run_tracing_basics_example() -> None:
    """演示 Agno 的 Tracing 基础能力。"""
    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "lesson_60_tracing.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    db = SqliteDb(db_file=str(db_path))

    try:
        from agno.tracing import setup_tracing

        setup_tracing(db=db, batch_processing=False)
        tracing_enabled = True
    except ImportError as exc:
        tracing_enabled = False
        print("\n--- Tracing 依赖缺失 ---")
        print(exc)

    model = OpenAIModel.from_env()
    agent = model.create_agent(
        name="Tracing Demo Agent",
        db=db,
        instructions=[
            "你是 Agno Tracing 示例助教。",
            "请简洁说明 tracing 能帮助观察哪些运行环节。",
        ],
        markdown=True,
    )

    response = agent.run(
        "请说明 tracing 在 Agent、Tools、Team、Workflow 里的价值。",
        user_id="student@example.com",
        session_id="lesson_60_tracing_demo",
    )
    print("\n--- Agent 响应 ---")
    print(response.content)

    print("\n--- Tracing 配置 ---")
    print(f"tracing_enabled: {tracing_enabled}")
    print(f"db_path: {db_path}")

    print("\n--- 关键观察点 ---")
    print("1. setup_tracing(db=...) 会安装 Agno 的 OpenTelemetry instrumentation。")
    print("2. Agent、Team、Workflow、工具调用和模型调用都可以被自动追踪。")
    print("3. DatabaseSpanExporter 会把 trace 写入 Agno 数据库。")
    print("4. 本地需要安装 opentelemetry / openinference 相关依赖才会真正启用。")


if __name__ == "__main__":
    run_tracing_basics_example()
