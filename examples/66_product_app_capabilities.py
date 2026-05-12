import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from study_assistant_app.product_app import (
    StudyAssistantProductConfig,
    create_study_assistant_product_app,
)


PRODUCT_CONFIG = StudyAssistantProductConfig(
    enable_scheduler=True,
    enable_interfaces=True,
    enable_skills=True,
    enable_guardrails=True,
    enable_tracing=False,
    enable_mcp_docs=False,
)


def create_app():
    """创建第 66 课使用的 FastAPI app。"""
    return create_study_assistant_product_app(PRODUCT_CONFIG)


def describe_product_config() -> StudyAssistantProductConfig:
    """返回本课产品入口配置，便于直接运行时查看。"""
    return PRODUCT_CONFIG


def run_product_app_capabilities_example() -> None:
    """输出这一课的运行说明。"""
    config = describe_product_config()
    print("这是一节‘回到 study_assistant_app 做产品化整理’课程。")
    print("启动方式：")
    print("fastapi dev examples/66_product_app_capabilities.py")
    print("")
    print("当前配置：")
    print(config)
    print("")
    print("启动后可以查看：")
    print("- OpenAPI 文档: http://127.0.0.1:8000/docs")
    print("- 产品健康检查: http://127.0.0.1:8000/study-assistant/product/health")
    print("- 产品配置概览: http://127.0.0.1:8000/study-assistant/product/config")
    print("")
    print("这节课建议重点观察：")
    print("1. product_app.py 如何把 Agent / Team / Workflow / Scheduler 继续保留为统一入口")
    print("2. Skills 如何作为学习规划能力包注入产品教练 Agent")
    print("3. Guardrails 如何作为 pre_hooks 进入产品安全边界")
    print("4. Tracing 和 MCP 如何作为可选能力，通过配置开关渐进启用")
    print("5. /study-assistant/product/config 如何暴露产品能力状态")
    print("")
    print("如需尝试 MCP 文档工具，请先安装依赖并改为 enable_mcp_docs=True：")
    print("uv pip install mcp")


if __name__ == "__main__":
    run_product_app_capabilities_example()
