from models import OpenAIModel

from .knowledge import build_study_knowledge
from .team import build_study_team


def run_study_assistant_app() -> None:
    """运行模块化后的学习助手小应用。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_study_knowledge()
    team = build_study_team(model_wrapper, knowledge)

    # 这个问题会触发知识检索、工具调用和 Team 协调。
    team.print_response(
        "我已经学完了 Agent、Tools、Knowledge、Team 以及整合课。"
        "请结合共享知识库，帮我总结我现在处于什么阶段，"
        "这个阶段的学习难度如何，以及下一课最适合学什么。"
    )
