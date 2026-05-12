"""Human in the Loop 基础示例。

演示 Agno 的 Human in the Loop 能力，包括：
1. requires_confirmation：工具执行前需要用户确认
2. requires_user_input：工具执行前需要用户补充字段
3. external_execution：工具交给外部系统执行
4. 观察 RunOutput.requirements
"""

from agno.tools.decorator import tool

from models import OpenAIModel


@tool(requires_confirmation=True)
def publish_learning_plan(plan_title: str) -> str:
    """发布学习计划。"""
    return f"已发布学习计划：{plan_title}"


@tool(requires_user_input=True, user_input_fields=["review_date"])
def schedule_review(topic: str, review_date: str) -> str:
    """安排复习提醒。"""
    return f"已为 {topic} 安排复习日期：{review_date}"


@tool(external_execution=True)
def create_external_ticket(title: str) -> str:
    """创建一个需要外部系统执行的工单。"""
    return f"外部工单已创建：{title}"


def print_requirements(response) -> None:
    """打印 HITL 暂停需求。"""
    requirements = response.requirements or []
    print(f"\n--- requirements 数量: {len(requirements)} ---")
    for index, requirement in enumerate(requirements, 1):
        print(f"{index}. {requirement.to_dict()}")


def run_human_in_the_loop_basics_example() -> None:
    """演示 Agno 的 Human in the Loop 基础能力。"""
    model = OpenAIModel.from_env()
    agent = model.create_agent(
        name="HITL Agent",
        tools=[publish_learning_plan, schedule_review, create_external_ticket],
        instructions=[
            "你是 Human in the Loop 示例助教。",
            "当用户要求发布、安排复习或创建外部工单时，请调用合适工具。",
        ],
        markdown=True,
        debug_mode=True,
    )

    confirm_response = agent.run(
        "请发布一个标题为 Hooks 复盘计划 的学习计划。",
        user_id="student@example.com",
        session_id="lesson_58_confirmation_demo",
    )
    print_requirements(confirm_response)

    input_response = agent.run(
        "请为 Guardrails 安排复习，但我还没有告诉你日期。",
        user_id="student@example.com",
        session_id="lesson_58_user_input_demo",
    )
    print_requirements(input_response)

    external_response = agent.run(
        "请创建一个外部工单：把学习进度同步到项目管理系统。",
        user_id="student@example.com",
        session_id="lesson_58_external_execution_demo",
    )
    print_requirements(external_response)

    print("\n--- 关键观察点 ---")
    print("1. requires_confirmation 适合发布、删除、付款等需要确认的动作。")
    print("2. requires_user_input 适合工具参数缺失时暂停等待用户补充。")
    print("3. external_execution 适合把动作交给 UI、队列或第三方系统执行。")
    print("4. response.requirements 记录了当前运行暂停等待的人工步骤。")


if __name__ == "__main__":
    run_human_in_the_loop_basics_example()
