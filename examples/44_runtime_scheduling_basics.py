from study_assistant_app.runtime_scheduling_app import create_study_assistant_runtime_scheduling_app


# 这一课继续沿 Runtime 主线推进：
# 重点观察 AgentOS scheduler、startup-registered schedule 和 SchedulerTools。
app = create_study_assistant_runtime_scheduling_app()


def run_runtime_scheduling_basics_example() -> None:
    """输出这一课的运行说明。"""
    print("这是一节 Scheduling 课程。")
    print("启动方式：")
    print("fastapi dev examples/44_runtime_scheduling_basics.py")
    print("")
    print("启动后可以查看：")
    print("- OpenAPI 文档: http://127.0.0.1:8000/docs")
    print("- 调度概览: http://127.0.0.1:8000/study-assistant/scheduling/overview")
    print("")
    print("这节课建议重点观察：")
    print("1. AgentOS 如何开启 scheduler=True")
    print("2. 应用启动时如何注册固定 schedule")
    print("3. agent 如何通过 SchedulerTools 创建调度任务")
    print("4. 调度最终命中的其实仍然是 agent / workflow 的运行端点")
    print("")
    print("启动服务后，你还可以重点查看这些接口：")
    print("- GET /schedules")
    print("- POST /schedules")
    print("- POST /schedules/{schedule_id}/trigger")


if __name__ == "__main__":
    run_runtime_scheduling_basics_example()
