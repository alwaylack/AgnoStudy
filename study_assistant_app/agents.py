from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge

from models import OpenAIModel

from .tools import estimate_stage_difficulty, suggest_next_lesson


def build_research_agent(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Agent:
    """创建负责知识检索和概念梳理的成员。"""
    return model_wrapper.create_agent(
        name="知识研究成员",
        role="负责从知识库中提取重点并解释概念。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你负责先理解问题，再从知识库中提取最相关的信息。",
            "请尽量基于资料内容回答，不要脱离知识库随意扩展。",
        ],
        markdown=True,
    )


def build_planning_agent(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Agent:
    """创建负责学习规划和下一步建议的成员。"""
    return model_wrapper.create_agent(
        name="学习规划成员",
        role="负责评估难度并给出下一步学习建议。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        tools=[estimate_stage_difficulty, suggest_next_lesson],
        instructions=[
            "你负责把知识库信息整理成清晰的学习建议。",
            "当问题涉及难度判断或下一课安排时，请优先调用工具。",
        ],
        markdown=True,
    )
