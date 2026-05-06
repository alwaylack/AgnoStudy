from study_assistant_app.runtime_storage_interfaces_app import (
    create_study_assistant_runtime_storage_interfaces_app,
)


# 这一课继续沿 Runtime 主线推进：
# 重点观察统一 db、条件接口注册，以及 one-off webhook 路由。
app = create_study_assistant_runtime_storage_interfaces_app()


def run_runtime_storage_interfaces_basics_example() -> None:
    """输出这一课的运行说明。"""
    print("这是一节 Runtime: Storage + Interfaces 课程。")
    print("启动方式：")
    print("fastapi dev examples/43_runtime_storage_interfaces_basics.py")
    print("")
    print("启动后可以查看：")
    print("- OpenAPI 文档: http://127.0.0.1:8000/docs")
    print("- Runtime 概览: http://127.0.0.1:8000/study-assistant/runtime/overview")
    print("")
    print("这节课建议重点观察：")
    print("1. 一个 db 如何承载 Runtime 状态")
    print("2. 接口如何按凭据条件注册")
    print("3. 自定义 webhook 如何直接挂到 FastAPI app 上")
    print("")
    print("你还可以测试这个自定义 webhook：")
    print("POST /study-assistant/webhooks/lesson-note")


if __name__ == "__main__":
    run_runtime_storage_interfaces_basics_example()
