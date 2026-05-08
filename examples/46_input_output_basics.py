from pathlib import Path

from pydantic import BaseModel, Field

from models import OpenAIModel


class StudyRequest(BaseModel):
    """定义输入给 Agent 的结构化学习请求。"""

    topic: str = Field(description="本次学习主题")
    current_stage: str = Field(description="当前学习阶段")
    goals: list[str] = Field(description="这次希望完成的目标")
    available_minutes: int = Field(description="本次可投入的学习时长，单位是分钟")


class StudyOutput(BaseModel):
    """定义 Agent 返回的结构化学习结果。"""

    summary: str = Field(description="对当前学习请求的简短总结")
    recommended_next_step: str = Field(description="最推荐的下一步动作")
    key_points: list[str] = Field(description="2 到 4 条关键学习要点")
    practice_task: str = Field(description="一个可以立刻执行的练习任务")


def run_input_output_basics_example() -> None:
    """演示 Agno 的 Input & Output 基础能力。"""
    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "tmp"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "lesson_46_input_output_result.md"

    model = OpenAIModel.from_env()

    # 这一课把官方 Input & Output 里最常用的四个点放在一起：
    # 1. input_schema：约束输入结构
    # 2. expected_output：补充输出预期
    # 3. output_schema：约束返回结构
    # 4. save_response_to_file：把最终结果自动保存到文件
    agent = model.create_agent(
        name="Agno Input Output Agent",
        instructions=[
            "你是 Agno 学习助教。",
            "请根据输入的学习请求，输出清晰、可执行、适合当前学习阶段的建议。",
            "输出内容要简洁，不要写成长篇大论。",
        ],
        input_schema=StudyRequest,
        expected_output="返回一份适合当前学习阶段的简洁学习建议，强调下一步动作和可执行练习。",
        output_schema=StudyOutput,
        use_json_mode=True,
        markdown=True,
        save_response_to_file=str(output_file),
    )

    # 官方文档里 input_schema 支持 dict 和 Pydantic 模型。
    # 这里先用 dict，方便你直接看到“结构化输入”最基础的传法。
    response = agent.run(
        input={
            "topic": "Agno Input & Output",
            "current_stage": "已经学到 Runtime 和产品化入口",
            "goals": [
                "理解结构化输入和结构化输出的区别",
                "学会把结果保存到文件",
                "为后续 Database 课程做准备",
            ],
            "available_minutes": 40,
        }
    )

    print("\n--- 结构化输出结果 ---")
    print(response.content)
    print("\n--- 保存路径 ---")
    print(output_file)


if __name__ == "__main__":
    run_input_output_basics_example()
