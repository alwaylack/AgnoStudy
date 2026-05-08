from study_assistant_app.product_app import create_study_assistant_product_app


# 这一课把前面补过的 Runtime 能力收拢成一个统一应用入口。
app = create_study_assistant_product_app()


def run_product_app_basics_example() -> None:
    """输出这一课的运行说明。"""
    print("这是一节‘回到更完整的小项目升级’课程。")
    print("启动方式：")
    print("fastapi dev examples/45_product_app_basics.py")
    print("")
    print("启动后可以查看：")
    print("- OpenAPI 文档: http://127.0.0.1:8000/docs")
    print("- 产品健康检查: http://127.0.0.1:8000/study-assistant/product/health")
    print("- 产品配置概览: http://127.0.0.1:8000/study-assistant/product/config")
    print("")
    print("这节课建议重点观察：")
    print("1. 一个统一 app 如何承载 agent / team / workflow / scheduler")
    print("2. 一个统一 db 如何支撑 Runtime 运行态")
    print("3. 为什么这一步比单独示例更接近真实小项目")


if __name__ == "__main__":
    run_product_app_basics_example()
