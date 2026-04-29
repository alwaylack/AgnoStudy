from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType
from agno.workflow import Step, Workflow

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_team_workflow_knowledge() -> Knowledge:
    """构建供 Workflow + Team + Knowledge 示例使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_workflow_team_knowledge"
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
        collection="agno_workflow_team_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=OpenAICompatibleEmbedder.from_env().get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_workflow_team_knowledge",
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


def build_knowledge_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建围绕共享知识库协作分析的团队。"""
    concept_agent = model_wrapper.create_agent(
        name="知识概念成员",
        role="负责解释当前问题里最重要的概念关系。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请先基于共享知识库解释当前最关键的概念。",
            "回答时优先使用知识库里能支撑当前问题的内容。",
        ],
        markdown=True,
    )

    roadmap_agent = model_wrapper.create_agent(
        name="学习路线成员",
        role="负责基于共享知识库安排下一阶段学习路线。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请根据共享知识库里的资料，给出下一阶段最适合的学习安排。",
            "回答时说明为什么这样安排。",
        ],
        markdown=True,
    )

    return Team(
        name="Workflow 知识协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[concept_agent, roadmap_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是一个围绕共享知识库协作的学习团队。",
            "请协调不同成员，从概念理解和路线规划两个角度共同完成分析。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )


def run_workflow_team_knowledge_basics_example() -> None:
    """运行 Workflow + Team + Knowledge 入门示例。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_team_workflow_knowledge()

    kickoff_agent = model_wrapper.create_agent(
        name="流程背景整理员",
        role="负责识别当前学习背景和本次目标。",
        instructions=[
            "请先识别用户当前已经学到了哪里，以及这次请求想解决什么问题。",
            "输出尽量简洁，作为后续知识协作阶段的上下文。",
        ],
        markdown=True,
    )

    summary_agent = model_wrapper.create_agent(
        name="最终建议汇总员",
        role="负责整合 Workflow、Team 和 Knowledge 阶段结果。",
        instructions=[
            "你会收到前面流程的背景整理结果，以及团队基于知识库的协作结果。",
            "请整合这些信息，给出最终的下一阶段学习建议。",
        ],
        markdown=True,
    )

    knowledge_team = build_knowledge_team(model_wrapper, knowledge)

    workflow = Workflow(
        name="Agno Workflow + Team + Knowledge 基础课",
        description="学习如何把 Workflow、Team、Knowledge 三者组合在同一个工作流里。",
        steps=[
            Step(
                name="流程背景整理",
                agent=kickoff_agent,
                description="先识别当前学习背景和本次目标。",
            ),
            Step(
                name="知识协作分析阶段",
                team=knowledge_team,
                description="让 Team 基于共享知识库协作完成核心分析。",
            ),
            Step(
                name="最终综合建议",
                agent=summary_agent,
                description="整合流程背景和知识协作结果，给出最终建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel、Loop、"
            "多模式组合课，以及 Workflow + Team 和 Workflow + Knowledge。"
            "请用 Workflow + Team + Knowledge 的方式，帮我安排下一阶段学习。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_team_knowledge_basics_example()
