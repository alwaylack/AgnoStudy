"""Skills 基础示例。

演示 Agno 的 Skills 能力，包括：
1. 从本地目录加载 SKILL.md
2. 观察 Skills 生成的系统提示片段
3. 让 Agent 按需读取 skill instructions / references
4. 对比 Skills 和普通 tools 的职责差异
"""

from pathlib import Path

from agno.skills import LocalSkills, Skills

from models import OpenAIModel


def build_local_skills() -> Skills:
    """加载本节课提供的本地 skill。"""
    skills_dir = Path(__file__).resolve().parent / "skills"
    return Skills(loaders=[LocalSkills(path=str(skills_dir), validate=False)])


def print_loaded_skills(skills: Skills) -> None:
    """打印当前加载的 skill 列表。"""
    print("\n--- 已加载 Skills ---")
    for skill in skills.get_all_skills():
        print(f"- {skill.name}: {skill.description}")
        print(f"  references: {skill.references or 'none'}")
        print(f"  scripts: {skill.scripts or 'none'}")


def run_skill_loader_demo() -> None:
    """场景一：程序化加载并查看本地 skills。"""
    skills = build_local_skills()
    print_loaded_skills(skills)

    snippet = skills.get_system_prompt_snippet()
    print("\n--- Skills 系统提示片段预览 ---")
    print(snippet[:600])


def run_agent_skill_demo() -> None:
    """场景二：Agent 通过 Skills 工具按需读取 skill 内容。"""
    model = OpenAIModel.from_env()
    skills = build_local_skills()

    agent = model.create_agent(
        name="Agno Skills Agent",
        skills=skills,
        instructions=[
            "你是 Agno Skills 示例的学习助教。",
            "当任务匹配可用 skill 时，先调用 get_skill_instructions。",
            "如果需要检查清单，再调用 get_skill_reference。",
        ],
        markdown=True,
        debug_mode=True,
    )

    response = agent.run(
        "请使用 agno_lesson_planner skill，帮我规划 Hooks 之后的下一节 Agno 课程。",
        user_id="student@example.com",
        session_id="lesson_54_skills_demo",
    )
    print("\n--- Agent 响应 ---")
    print(response.content)


def run_skills_basics_example() -> None:
    """演示 Agno 的 Skills 基础能力。"""
    run_skill_loader_demo()
    run_agent_skill_demo()

    print("\n--- 关键观察点 ---")
    print("1. Skill 是可按需加载的领域能力包，不是直接调用的工具函数。")
    print("2. Skills 会把可用 skill 摘要放进系统提示。")
    print("3. Agent 会通过 get_skill_instructions / get_skill_reference 渐进读取细节。")
    print("4. Skill 适合沉淀流程、规范、参考文档和脚本模板。")


if __name__ == "__main__":
    run_skills_basics_example()
