from agno.tools import Toolkit

from models import OpenAIModel


class StudyTools(Toolkit):
    """把多个学习相关工具打包成一个可复用的 Toolkit。"""

    def __init__(self) -> None:
        super().__init__(name="study_tools")

        # 在自定义 Toolkit 中，需要把方法显式注册成工具。
        self.register(self.get_study_tip)
        self.register(self.make_daily_goal)
        self.register(self.add_numbers)

    def get_study_tip(self, topic: str) -> str:
        """根据主题返回一条学习建议。"""
        tips = {
            "agent": "先理解 Agent 的核心职责，再学习记忆和工具。",
            "memory": "重点观察同一个 user_id 在不同 session_id 下的表现。",
            "tools": "先从简单函数工具开始，再组合成 Toolkit。",
        }
        return tips.get(topic.lower(), f"学习 {topic} 时，建议先从最小可运行示例开始。")

    def make_daily_goal(self, topic: str, minutes: int) -> str:
        """根据主题和时长生成一个简单的今日目标。"""
        return f"今天用 {minutes} 分钟学习 {topic}，重点是跑通一个最小示例并理解输出。"

    def add_numbers(self, a: int, b: int) -> int:
        """返回两个整数的和。"""
        return a + b


def run_custom_toolkit_example() -> None:
    """演示如何把自定义 Toolkit 注册到 Agent。"""
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Custom Toolkit Agent",
        tools=[StudyTools()],
        instructions=[
            "你是 Agno 学习助手。",
            "遇到适合用工具完成的问题时，优先调用工具。",
            "回答时请顺带说明刚刚调用了什么工具。",
        ],
        markdown=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：调用自定义学习建议工具 ---")
    agent.print_response("我在学习 Agno 的 memory，请给我一条学习建议。")

    print("\n--- 示例 2：调用自定义计划工具 ---")
    agent.print_response("帮我制定一个今天学习 toolkit 的 30 分钟目标。")

    print("\n--- 示例 3：调用自定义计算工具 ---")
    agent.print_response("请帮我计算 8 + 14，并说明这是如何通过自定义工具完成的。")


if __name__ == "__main__":
    run_custom_toolkit_example()
