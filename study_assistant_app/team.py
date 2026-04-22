from agno.knowledge.knowledge import Knowledge
from agno.team import Team, TeamMode

from models import OpenAIModel

from .agents import build_planning_agent, build_research_agent


def build_study_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """创建一个共享知识库的小型学习助手团队。"""
    research_agent = build_research_agent(model_wrapper, knowledge)
    planning_agent = build_planning_agent(model_wrapper, knowledge)

    return Team(
        name="Agno 学习助手团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[research_agent, planning_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        add_member_tools_to_context=True,
        instructions=[
            "你是一个学习助手团队协调者。",
            "请先理解用户当前进度，再调用合适成员完成分析。",
            "最终回答需要同时包含进度判断、重点总结和下一步建议。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )
