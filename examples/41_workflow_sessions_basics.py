from pathlib import Path

from agno.db.sqlite import SqliteDb
from agno.run import RunContext
from agno.workflow import Step, StepInput, StepOutput, Workflow

from models import OpenAIModel


def update_study_session_state(step_input: StepInput, run_context: RunContext) -> StepOutput:
    """把当前输入里的学习进度写入 Workflow session_state。"""
    if not run_context.session_state:
        run_context.session_state = {}

    run_context.session_state.setdefault("completed_topics", [])
    run_context.session_state.setdefault("current_goal", "")
    run_context.session_state.setdefault("notes", [])

    user_input = str(step_input.input or "")
    lowered_input = user_input.lower()

    topic_mapping = {
        "workflow": "Workflow",
        "session": "Sessions",
        "history": "History",
        "runtime": "Runtime",
        "knowledge": "Knowledge",
        "team": "Team",
    }

    for keyword, topic_name in topic_mapping.items():
        if keyword in lowered_input and topic_name not in run_context.session_state["completed_topics"]:
            run_context.session_state["completed_topics"].append(topic_name)

    run_context.session_state["current_goal"] = user_input
    run_context.session_state["notes"].append(f"记录一条新的学习输入：{user_input}")

    content = (
        "已更新本次 Workflow Session 的学习状态。\n"
        f"当前已记录主题：{', '.join(run_context.session_state['completed_topics']) or '暂无'}\n"
        f"当前目标：{run_context.session_state['current_goal']}"
    )
    return StepOutput(content=content, success=True)


def inspect_study_session_state(step_input: StepInput, run_context: RunContext) -> StepOutput:
    """读取当前 Workflow session_state，帮助观察跨运行共享状态。"""
    session_state = run_context.session_state or {}
    completed_topics = session_state.get("completed_topics", [])
    notes = session_state.get("notes", [])

    content = (
        "当前 Session State 概览：\n"
        f"- 已记录主题：{', '.join(completed_topics) or '暂无'}\n"
        f"- 笔记条数：{len(notes)}\n"
        f"- 当前目标：{session_state.get('current_goal', '暂无')}"
    )
    return StepOutput(content=content, success=True)


def run_workflow_sessions_basics_example() -> None:
    """演示 Workflow Sessions、Workflow History 和 Session State。"""
    db_path = Path(__file__).resolve().parents[1] / "tmp" / "workflow_sessions.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model_wrapper = OpenAIModel.from_env()

    reflection_agent = model_wrapper.create_agent(
        name="Workflow Session 复盘成员",
        role="负责基于当前运行结果、之前的 Workflow history 和 session_state 给出学习建议。",
        instructions=[
            "你会收到当前步骤结果，并且 Workflow 可能会自动附带之前运行的历史结果。",
            "请基于这些历史结果和当前状态，给出更连续、更一致的下一步学习建议。",
            "回答时要明确说明：当前进度、历史延续点、下一步建议。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Workflow Sessions 基础课",
        description="学习如何在 Workflow 中持久化 session、启用 workflow history，并共享 session state。",
        db=SqliteDb(db_file=str(db_path)),
        session_state={
            "completed_topics": [],
            "current_goal": "",
            "notes": [],
        },
        add_workflow_history_to_steps=True,
        num_history_runs=3,
        steps=[
            Step(
                name="更新学习状态",
                executor=update_study_session_state,
                description="把本次输入同步到 Workflow session_state。",
            ),
            Step(
                name="查看共享状态",
                executor=inspect_study_session_state,
                description="查看当前 Workflow session_state 的内容。",
            ),
            Step(
                name="基于 Session 给出建议",
                agent=reflection_agent,
                description="结合 Workflow 历史和共享状态，输出连续的学习建议。",
            ),
        ],
        debug_mode=True,
    )

    user_id = "student@example.com"
    session_id = "workflow_sessions_demo"

    print("\n--- 第 1 次运行：建立第一条 Workflow Session 记录 ---")
    workflow.print_response(
        input="我已经学完了 Workflow、Team 和 Knowledge，现在想开始补 Session 这条官方主线。",
        user_id=user_id,
        session_id=session_id,
        markdown=True,
        stream=True,
        show_step_details=True,
    )

    try:
        workflow.set_session_name(session_id=session_id, session_name="Agno Workflow Sessions 学习记录")
        session_name = workflow.get_session_name(session_id=session_id)
        print(f"\n当前 Session 名称：{session_name}")
    except AttributeError:
        print("\n当前版本未提供 Workflow session 命名接口，跳过命名演示。")

    try:
        print("当前 Session State：", workflow.get_session_state())
    except AttributeError:
        print("当前版本未提供 get_session_state()，跳过直接读取演示。")

    print("\n--- 第 2 次运行：复用同一个 session_id，观察历史延续 ---")
    workflow.print_response(
        input="我还想重点理解 workflow history、session_state 和普通 agent history 的区别。",
        user_id=user_id,
        session_id=session_id,
        markdown=True,
        stream=True,
        show_step_details=True,
    )

    print("\n--- 第 3 次运行：继续同一个 Session，验证跨运行连续性 ---")
    workflow.print_response(
        input="请基于前两次 Workflow 运行记录，帮我安排下一课，优先接 Runtime 方向。",
        user_id=user_id,
        session_id=session_id,
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_sessions_basics_example()
