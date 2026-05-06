from study_assistant_app.runtime_api_app import create_study_assistant_runtime_app


# 这一课不是直接在脚本里跑一次对话，而是把现有能力暴露成可服务化的 FastAPI 应用。
# 按 Agno 官方 Runtime 路线，这个 app 可以直接被 fastapi dev 加载。
app = create_study_assistant_runtime_app()


def run_runtime_serve_api_basics_example() -> None:
    """输出这一课的运行说明。"""
    print("这是一节 Runtime / Serve as API 课程。")
    print("启动方式：")
    print("fastapi dev examples/42_runtime_serve_api_basics.py")
    print("")
    print("启动后可以查看：")
    print("- OpenAPI 文档: http://127.0.0.1:8000/docs")
    print("- 自定义健康检查: http://127.0.0.1:8000/study-assistant/health")
    print("")
    print("你还可以通过 AgentOS 自动生成的接口运行组件，例如：")
    print("- POST /agents/{agent_id}/runs")
    print("- POST /teams/{team_id}/runs")
    print("- POST /workflows/{workflow_id}/runs")


if __name__ == "__main__":
    run_runtime_serve_api_basics_example()
