from contextlib import asynccontextmanager
from pathlib import Path

from models import OpenAIModel

from .knowledge import build_study_knowledge
from .workflow_app import build_study_assistant_workflow_app


def create_study_assistant_runtime_scheduling_app():
    """创建带 Scheduler 的 AgentOS Runtime 应用。"""
    try:
        from agno.agent import Agent
        from agno.db.sqlite import SqliteDb
        from agno.os import AgentOS
        from agno.scheduler import ScheduleManager
        from agno.tools.scheduler import SchedulerTools
    except ImportError as exc:
        raise ImportError(
            "运行这一课前，请先安装调度依赖：`uv pip install -U \"agno[scheduler]\" fastapi uvicorn`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "study_assistant_scheduler.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    db = SqliteDb(db_file=str(db_path))
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_study_knowledge()
    workflow = build_study_assistant_workflow_app(model_wrapper)
    workflow_run_endpoint = f"/workflows/{workflow.id}/runs"

    scheduler_agent = Agent(
        id="study-scheduler-agent",
        name="学习计划调度助手",
        model=model_wrapper.get_model(),
        db=db,
        tools=[
            SchedulerTools(
                db=db,
                default_endpoint=workflow_run_endpoint,
                default_method="POST",
                default_timezone="Asia/Shanghai",
            )
        ],
        instructions=[
            "你负责帮助用户创建和管理学习计划调度任务。",
            "当用户想安排定时执行时，请优先使用 SchedulerTools。",
        ],
        markdown=True,
        debug_mode=True,
    )

    @asynccontextmanager
    async def lifespan(app, agent_os=None):
        # 这个版本里没有 register_schedule 这个便捷函数，
        # 所以直接用 ScheduleManager 往统一 db 中写入或更新调度记录。
        schedule_manager = ScheduleManager(db=db)
        schedule_manager.create(
            name="study_assistant_weekday_digest",
            cron="0 9 * * 1-5",
            endpoint=workflow_run_endpoint,
            method="POST",
            description="工作日早上 9 点生成一条 Agno 学习推进建议。",
            payload={"message": "请生成今天的 Agno 学习推进建议，并优先提醒 Runtime 主线。"},
            timezone="Asia/Shanghai",
            if_exists="update",
        )
        yield

    agent_os = AgentOS(
        agents=[scheduler_agent],
        workflows=[workflow],
        db=db,
        scheduler=True,
        scheduler_poll_interval=15,
        lifespan=lifespan,
    )

    app = agent_os.get_app()

    @app.get("/study-assistant/scheduling/overview")
    async def scheduling_overview():
        """说明当前调度课程的配置重点。"""
        return {
            "status": "ok",
            "db_backend": "sqlite",
            "db_file": str(db_path),
            "scheduler": {
                "enabled": True,
                "poll_interval_seconds": 15,
                "startup_schedule": "study_assistant_weekday_digest",
                "workflow_run_endpoint": workflow_run_endpoint,
            },
            "available_patterns": [
                "startup-registered schedule",
                "agent-driven scheduling with SchedulerTools",
            ],
        }

    @app.get("/study-assistant/health")
    async def study_assistant_health():
        """补一个健康检查路由，保持和前几课一致。"""
        return {
            "status": "ok",
            "service": "study-assistant-scheduler-runtime",
            "components": ["scheduler", "workflow", "agent"],
        }

    return app
