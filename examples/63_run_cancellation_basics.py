"""Run Cancellation 基础示例。

演示 Agno 的 Run Cancellation 能力，包括：
1. 显式注册 run_id
2. 调用 cancel_run 标记取消
3. 用 is_cancelled / raise_if_cancelled 检查取消状态
4. 清理取消追踪状态
"""

from agno.exceptions import RunCancelledException
from agno.run.cancel import cancel_run, cleanup_run, is_cancelled, raise_if_cancelled, register_run


def run_run_cancellation_basics_example() -> None:
    """演示 Agno 的 Run Cancellation 基础能力。"""
    run_id = "lesson_63_cancellable_run"

    register_run(run_id)
    print("\n--- 注册运行 ---")
    print(f"is_cancelled before cancel: {is_cancelled(run_id)}")

    cancelled = cancel_run(run_id)
    print("\n--- 取消运行 ---")
    print(f"cancel_run returned: {cancelled}")
    print(f"is_cancelled after cancel: {is_cancelled(run_id)}")

    print("\n--- 检查取消状态 ---")
    try:
        raise_if_cancelled(run_id)
    except RunCancelledException as exc:
        print(f"raise_if_cancelled 捕获到取消: {exc}")
    finally:
        cleanup_run(run_id)

    print("\n--- 清理后状态 ---")
    print(f"is_cancelled after cleanup: {is_cancelled(run_id)}")

    print("\n--- 关键观察点 ---")
    print("1. Agno 会在 Agent 运行过程中注册 run_id 并检查取消状态。")
    print("2. cancel_run(run_id) 标记某次运行需要取消。")
    print("3. raise_if_cancelled(run_id) 会把取消转换成 RunCancelledException。")
    print("4. 取消完成后要 cleanup_run(run_id)，避免状态残留。")


if __name__ == "__main__":
    run_run_cancellation_basics_example()
