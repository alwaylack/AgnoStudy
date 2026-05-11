"""State Management 基础示例。

演示 Agno 的状态管理能力，包括：
1. 手动管理状态（update_session_state）
2. Agent 自动管理状态（enable_agentic_state）
3. 状态注入上下文（add_session_state_to_context）
"""

from pathlib import Path

from agno.db.sqlite import SqliteDb

from models import OpenAIModel


# ---------------------------------------------------------------------------
# 辅助函数：状态显示
# ---------------------------------------------------------------------------

def print_task_state(state: dict, label: str = "当前任务状态") -> None:
    """格式化输出任务状态，便于观察。"""
    print(f"\n--- {label} ---")
    if not state:
        print("（状态为空）")
        return

    tasks = state.get("tasks", [])
    print(f"任务总数: {len(tasks)}")

    if not tasks:
        print("（暂无任务）")
        return

    for i, task in enumerate(tasks, 1):
        status_icon = "✅" if task.get("status") == "completed" else "⏳"
        priority = task.get("priority", "medium")
        priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(priority, "⚪")
        print(f"  {i}. {status_icon} {priority_icon} {task.get('title', '无标题')}")
        if task.get("description"):
            print(f"     描述: {task['description']}")


def print_state_snapshot(agent, session_id: str, label: str = "状态快照") -> None:
    """输出当前 session 的状态快照。"""
    state = agent.get_session_state(session_id=session_id)
    print_task_state(state, label)


# ---------------------------------------------------------------------------
# 场景一：手动管理状态
# ---------------------------------------------------------------------------

def run_manual_state_demo(
    model: OpenAIModel,
    db: SqliteDb,
) -> None:
    """演示手动管理 session state 的基础用法。"""
    print("\n" + "=" * 60)
    print("场景一：手动管理状态")
    print("=" * 60)

    agent = model.create_agent(
        name="Manual State Agent",
        db=db,
        instructions=[
            "你是任务管理助手，帮助用户管理待办事项。",
            "请简洁回答，聚焦于任务管理相关内容。",
        ],
        add_history_to_context=True,
        num_history_runs=2,
        markdown=True,
    )

    user_id = "student@example.com"
    session_id = "lesson_50_manual_state_demo"

    # 先运行一次创建 session
    print("\n--- 步骤 0：创建 session ---")
    agent.run(
        "你好，我是任务管理助手，请帮我初始化任务管理系统。",
        user_id=user_id,
        session_id=session_id,
    )

    # 初始化任务状态
    print("\n--- 步骤 1：初始化任务状态 ---")
    agent.update_session_state(
        session_state_updates={
            "tasks": [
                {
                    "id": "task_001",
                    "title": "学习 Agent 基础",
                    "description": "完成 Agent 基础示例代码",
                    "status": "completed",
                    "priority": "high",
                },
                {
                    "id": "task_002",
                    "title": "学习 Tools 使用",
                    "description": "掌握内置工具和自定义工具",
                    "status": "in_progress",
                    "priority": "high",
                },
            ],
            "project": "Agno 学习项目",
            "created_at": "2026-05-11",
        },
        session_id=session_id,
    )
    print_state_snapshot(agent, session_id, "初始化后的状态")

    # 手动添加新任务
    print("\n--- 步骤 2：添加新任务 ---")
    current_state = agent.get_session_state(session_id=session_id)
    tasks = current_state.get("tasks", [])
    tasks.append({
        "id": "task_003",
        "title": "学习 State Management",
        "description": "掌握 session state 的管理方式",
        "status": "pending",
        "priority": "medium",
    })
    agent.update_session_state(
        session_state_updates={"tasks": tasks},
        session_id=session_id,
    )
    print_state_snapshot(agent, session_id, "添加任务后的状态")

    # 手动更新任务状态
    print("\n--- 步骤 3：标记任务完成 ---")
    current_state = agent.get_session_state(session_id=session_id)
    tasks = current_state.get("tasks", [])
    for task in tasks:
        if task["id"] == "task_002":
            task["status"] = "completed"
    agent.update_session_state(
        session_state_updates={"tasks": tasks},
        session_id=session_id,
    )
    print_state_snapshot(agent, session_id, "完成任务后的状态")

    # 让 agent 基于状态回答问题
    print("\n--- 步骤 4：询问 agent 当前进度 ---")
    response = agent.run(
        "请总结一下我当前的学习进度和待办事项。",
        user_id=user_id,
        session_id=session_id,
        add_session_state_to_context=True,
    )
    print(f"助手: {response.content}")


# ---------------------------------------------------------------------------
# 场景二：Agent 自动管理状态
# ---------------------------------------------------------------------------

def run_agentic_state_demo(
    model: OpenAIModel,
    db: SqliteDb,
) -> None:
    """演示 agent 自动管理 session state 的高级用法。"""
    print("\n" + "=" * 60)
    print("场景二：Agent 自动管理状态")
    print("=" * 60)

    agent = model.create_agent(
        name="Agentic State Agent",
        db=db,
        session_state={"tasks": [], "project": "学习计划"},
        add_session_state_to_context=True,
        enable_agentic_state=True,
        instructions=[
            "你是智能任务管理助手，可以帮助用户管理待办事项。",
            "当用户提到新任务时，请自动添加到任务列表。",
            "当用户说完成某任务时，请自动更新任务状态。",
            "请保持任务列表整洁，及时归档已完成的任务。",
        ],
        markdown=True,
    )

    user_id = "student@example.com"
    session_id = "lesson_50_agentic_state_demo"

    # Agent 自动创建任务
    print("\n--- 第 1 轮：告诉 agent 新任务 ---")
    response1 = agent.run(
        "我今天需要完成三件事：学习 Context Management、复习 Session 管理、准备 State Management 课程。",
        user_id=user_id,
        session_id=session_id,
    )
    print(f"助手: {response1.content}")
    print_state_snapshot(agent, session_id, "Agent 自动创建的任务")

    # Agent 自动更新任务状态
    print("\n--- 第 2 轮：告诉 agent 已完成的任务 ---")
    response2 = agent.run(
        "我已经完成了 Context Management 的学习，Session 管理也复习好了。",
        user_id=user_id,
        session_id=session_id,
    )
    print(f"助手: {response2.content}")
    print_state_snapshot(agent, session_id, "Agent 自动更新后的状态")

    # Agent 调整任务优先级
    print("\n--- 第 3 轮：调整任务优先级 ---")
    response3 = agent.run(
        "State Management 课程很紧急，请把它标记为高优先级。",
        user_id=user_id,
        session_id=session_id,
    )
    print(f"助手: {response3.content}")
    print_state_snapshot(agent, session_id, "调整优先级后的状态")

    # Agent 基于状态提供建议
    print("\n--- 第 4 轮：询问下一步建议 ---")
    response4 = agent.run(
        "根据我当前的任务列表，你建议我下一步做什么？",
        user_id=user_id,
        session_id=session_id,
    )
    print(f"助手: {response4.content}")


# ---------------------------------------------------------------------------
# 场景三：状态注入上下文的效果
# ---------------------------------------------------------------------------

def run_state_context_demo(
    model: OpenAIModel,
    db: SqliteDb,
) -> None:
    """演示状态注入上下文对 agent 响应的影响。"""
    print("\n" + "=" * 60)
    print("场景三：状态注入上下文的效果")
    print("=" * 60)

    # 创建两个 agent，一个启用状态注入，一个不启用
    agent_with_state = model.create_agent(
        name="State-Aware Agent",
        db=db,
        session_state={
            "tasks": [
                {"title": "学习 Python", "status": "completed", "priority": "high"},
                {"title": "学习 Agno", "status": "in_progress", "priority": "high"},
                {"title": "构建项目", "status": "pending", "priority": "medium"},
            ],
            "current_focus": "Agno 框架",
        },
        add_session_state_to_context=True,
        instructions=["你是学习助手，请基于用户的当前状态提供个性化建议。"],
        markdown=True,
    )

    agent_without_state = model.create_agent(
        name="State-Unaware Agent",
        db=db,
        session_state={
            "tasks": [
                {"title": "学习 Python", "status": "completed", "priority": "high"},
                {"title": "学习 Agno", "status": "in_progress", "priority": "high"},
                {"title": "构建项目", "status": "pending", "priority": "medium"},
            ],
            "current_focus": "Agno 框架",
        },
        add_session_state_to_context=False,  # 不注入状态到上下文
        instructions=["你是学习助手，请提供学习建议。"],
        markdown=True,
    )

    user_id = "student@example.com"
    session_id_with = "lesson_50_state_with_context"
    session_id_without = "lesson_50_state_without_context"

    question = "我应该优先学习什么？"

    print(f"\n问题: {question}")

    print("\n--- 启用状态注入的 Agent ---")
    print("（可以看到 agent 基于当前任务状态回答）")
    response1 = agent_with_state.run(
        question,
        user_id=user_id,
        session_id=session_id_with,
    )
    print(f"助手: {response1.content}")

    print("\n--- 未启用状态注入的 Agent ---")
    print("（agent 无法感知当前任务状态）")
    response2 = agent_without_state.run(
        question,
        user_id=user_id,
        session_id=session_id_without,
    )
    print(f"助手: {response2.content}")

    print("\n--- 对比分析 ---")
    print("启用 add_session_state_to_context=True 后，agent 能够：")
    print("1. 看到当前的任务列表和状态")
    print("2. 基于实际进度给出个性化建议")
    print("3. 避免重复已完成的任务")


# ---------------------------------------------------------------------------
# 主函数
# ---------------------------------------------------------------------------

def run_state_management_basics_example() -> None:
    """演示 Agno 的 State Management 基础能力。"""
    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "lesson_50_state_management.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # 创建数据库，使用单独的 session_table 便于观察
    db = SqliteDb(
        db_file=str(db_path),
        session_table="lesson_50_agent_sessions",
    )

    model = OpenAIModel.from_env()

    # 场景一：手动管理状态
    run_manual_state_demo(model=model, db=db)

    # 场景二：Agent 自动管理状态
    run_agentic_state_demo(model=model, db=db)

    # 场景三：状态注入上下文的效果
    run_state_context_demo(model=model, db=db)

    print("\n" + "=" * 60)
    print("State Management 基础示例完成")
    print("=" * 60)
    print(f"\n数据库文件路径: {db_path}")
    print("\n关键观察点：")
    print("1. update_session_state() 用于手动管理状态")
    print("2. enable_agentic_state=True 让 agent 自动修改状态")
    print("3. add_session_state_to_context=True 将状态注入上下文")
    print("4. 状态注入可以显著提升 agent 的个性化响应能力")


if __name__ == "__main__":
    run_state_management_basics_example()
