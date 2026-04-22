from pydantic import BaseModel, Field

from models import OpenAIModel


class StudyTask(BaseModel):
    """定义单个学习任务的数据结构。"""

    title: str = Field(description="任务标题")
    duration_minutes: int = Field(description="预计学习时长，单位为分钟")
    goal: str = Field(description="这个任务的学习目标")


class DailyStudyPlan(BaseModel):
    """定义一天学习计划的结构化输出格式。"""

    topic: str = Field(description="今天学习的主题")
    level: str = Field(description="学习难度，例如入门、基础、进阶")
    tasks: list[StudyTask] = Field(description="今天的学习任务列表")
    summary: str = Field(description="对今天计划的简短总结")


def run_structured_output_example() -> None:
    """演示如何让 Agent 按固定结构返回结果。"""
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Structured Output Agent",
        instructions=[
            "你是 Agno 学习规划助手。",
            "请严格按照给定的数据结构返回结果。",
            "任务安排要适合刚学完 tools 基础的学习者。",
        ],
        output_schema=DailyStudyPlan,
        # 对 OpenAI 兼容模型来说，JSON 模式通常比原生结构化输出更稳。
        use_json_mode=True,
        markdown=True,
    )

    response = agent.run("帮我制定一个今天继续学习 Agno 的计划，重点是结构化输出。")

    print("\n--- 结构化输出结果 ---")
    print(response.content)


if __name__ == "__main__":
    run_structured_output_example()
