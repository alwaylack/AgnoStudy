from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType
from agno.workflow import Condition, Step, Workflow

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_mini_workflow_knowledge() -> Knowledge:
    """构建小型学习助手工作流使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_learning_assistant_workflow"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_tools_notes.md",
        knowledge_dir / "agno_memory_notes.md",
        knowledge_dir / "agno_beginner_track.md",
        knowledge_dir / "agno_advanced_track.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档：{document_path}")

    vector_db = ChromaDb(
        collection="agno_learning_assistant_workflow",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=OpenAICompatibleEmbedder.from_env().get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_learning_assistant_workflow",
        vector_db=vector_db,
    )

    reader = MarkdownReader(chunk_size=1200)
    for document_path in documents:
        knowledge.insert(
            path=str(document_path),
            reader=reader,
            upsert=True,
        )

    return knowledge


def estimate_weekly_effort(stage_name: str) -> str:
    """根据阶段给出建议的每周投入。"""
    stage = stage_name.lower()
    if "advanced" in stage or "workflow" in stage:
        return "建议每周投入 4 到 6 小时，保持连续练习。"
    if "beginner" in stage:
        return "建议每周投入 2 到 4 小时，先保证基础跑通。"
    return "建议每周投入 3 到 5 小时，根据理解速度动态调整。"


def suggest_output_style(goal: str) -> str:
    """根据目标给出更合适的学习产出形式。"""
    lowered_goal = goal.lower()
    if "workflow" in lowered_goal:
        return "更适合的产出是一个最小可运行工作流示例。"
    if "knowledge" in lowered_goal:
        return "更适合的产出是一个带知识库检索的可运行示例。"
    return "更适合的产出是一个能跑通的最小示例加一份阶段总结。"


def needs_advanced_path(step_input) -> bool:
    """根据当前输入判断是否进入进阶学习路径。"""
    user_input = (step_input.input or "").lower()
    advanced_keywords = ["workflow", "team", "knowledge", "parallel", "loop", "condition"]
    return any(keyword in user_input for keyword in advanced_keywords)


def build_beginner_path_note(step_input) -> StepOutput:
    """生成巩固路径说明。"""
    return StepOutput(
        content=(
            "当前进入巩固路径。\n"
            "建议先回顾已学模式的边界和职责，再逐步进入更完整的小型工作流。"
        ),
        success=True,
    )


def build_advanced_path_note(step_input) -> StepOutput:
    """生成进阶路径说明。"""
    return StepOutput(
        content=(
            "当前进入进阶路径。\n"
            "建议开始围绕一个真实学习助手目标，组织完整工作流并产出可执行计划。"
        ),
        success=True,
    )


def build_learning_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建围绕学习规划协作的知识团队。"""
    concept_agent = model_wrapper.create_agent(
        name="学习概念成员",
        role="负责解释当前阶段最该理解的关键概念。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请先基于共享知识库解释当前阶段最重要的概念重点。",
            "回答时尽量围绕当前阶段最需要理解的内容展开。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="学习规划成员",
        role="负责制定下一阶段学习安排。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        tools=[estimate_weekly_effort, suggest_output_style],
        instructions=[
            "请基于共享知识库制定下一阶段学习安排。",
            "当问题涉及学习投入或产出形式时，请优先调用工具。",
        ],
        markdown=True,
    )

    return Team(
        name="学习助手协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[concept_agent, planning_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        add_member_tools_to_context=True,
        instructions=[
            "你是一个围绕共享知识库协作的学习助手团队。",
            "请从概念理解和学习规划两个角度共同完成分析。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )


def run_learning_assistant_mini_workflow_example() -> None:
    """运行更接近真实项目的小型学习助手工作流。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_mini_workflow_knowledge()

    intake_agent = model_wrapper.create_agent(
        name="需求识别员",
        role="负责识别用户当前进度、目标和问题。",
        instructions=[
            "请先识别用户当前学到了哪里，以及现在最想解决的问题是什么。",
            "输出尽量简洁，作为后续工作流阶段的上下文。",
        ],
        markdown=True,
    )

    summary_agent = model_wrapper.create_agent(
        name="最终计划汇总员",
        role="负责把前面各阶段结果整理成一份可执行计划。",
        instructions=[
            "你会收到前面多个阶段的结果。",
            "请整合这些内容，给出一份可执行的下一阶段学习计划。",
            "最终回答要包含：当前阶段判断、学习重点、每周投入建议、下一课安排、建议产出形式。",
        ],
        markdown=True,
    )

    study_team = build_learning_team(model_wrapper, knowledge)

    workflow = Workflow(
        name="Agno 学习助手小型工作流",
        description="一个更接近真实项目的学习助手最小工作流。",
        steps=[
            Step(
                name="需求识别阶段",
                agent=intake_agent,
                description="先识别当前学习背景与本次目标。",
            ),
            Condition(
                name="学习路径判断",
                description="判断当前更适合巩固还是继续进阶。",
                evaluator=needs_advanced_path,
                steps=[
                    Step(
                        name="进阶路径说明",
                        executor=build_advanced_path_note,
                        description="进入进阶路径时补充一条路径说明。",
                    )
                ],
                else_steps=[
                    Step(
                        name="巩固路径说明",
                        executor=build_beginner_path_note,
                        description="进入巩固路径时补充一条路径说明。",
                    )
                ],
            ),
            Step(
                name="知识协作规划阶段",
                team=study_team,
                description="让团队基于共享知识库协作完成核心分析和规划。",
            ),
            Step(
                name="最终学习计划",
                agent=summary_agent,
                description="整合所有阶段结果，输出最终可执行计划。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel、Loop、"
            "多模式组合课，以及 Workflow + Team、Workflow + Knowledge、Workflow + Team + Knowledge。"
            "现在我想进入更接近真实项目的小型工作流阶段，请帮我安排下一阶段学习计划。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_learning_assistant_mini_workflow_example()
