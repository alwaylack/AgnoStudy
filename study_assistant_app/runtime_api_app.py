from pathlib import Path

from models import OpenAIModel

from .agents import build_research_agent
from .knowledge import build_study_knowledge
from .team import build_study_team
from .workflow_app import build_study_assistant_workflow_app


def create_study_assistant_runtime_app():
    """创建学习助手的 AgentOS Runtime 应用。"""
    try:
        from agno.db.sqlite import SqliteDb
        from agno.os import AgentOS
    except ImportError as exc:
        raise ImportError(
            "运行这一课前，请先安装 Runtime 依赖：`uv pip install -U \"agno[os]\" fastapi uvicorn`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "study_assistant_runtime.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model_wrapper = OpenAIModel.from_env()
    knowledge = build_study_knowledge()

    research_agent = build_research_agent(model_wrapper, knowledge)
    study_team = build_study_team(model_wrapper, knowledge)
    workflow = build_study_assistant_workflow_app(model_wrapper)

    agent_os = AgentOS(
        agents=[research_agent],
        teams=[study_team],
        workflows=[workflow],
        db=SqliteDb(db_file=str(db_path)),
    )

    app = agent_os.get_app()

    @app.get("/study-assistant/health")
    async def study_assistant_health():
        """补一个自定义健康检查路由，帮助理解 Runtime 也是 FastAPI 应用。"""
        return {
            "status": "ok",
            "service": "study-assistant-runtime",
            "components": ["agent", "team", "workflow"],
        }

    return app
