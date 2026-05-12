"""Evals 基础示例。

演示 Agno 的 Evals 能力，包括：
1. 用 AccuracyEval 描述输入、期望输出和被测 Agent
2. 用 run_with_output 评估已有输出
3. 用 PerformanceEval 评估普通函数性能
4. 区分模型质量评估和工程性能评估
"""

from agno.eval.accuracy import AccuracyEval
from agno.eval.performance import PerformanceEval

from models import OpenAIModel


def build_eval_agent():
    """构建一个被评估的最小 Agent。"""
    model = OpenAIModel.from_env()
    return model.create_agent(
        name="Eval Target Agent",
        instructions=[
            "你是 Agno 课程问答助手。",
            "回答要准确、简洁。",
        ],
        markdown=True,
    )


def run_accuracy_eval_demo() -> None:
    """场景一：用 AccuracyEval 评估已有输出。"""
    agent = build_eval_agent()
    eval_case = AccuracyEval(
        name="lesson_59_accuracy_eval",
        input="Agno Hooks 主要解决什么问题？",
        expected_output="Hooks 用于在 Agent 或 Team 运行前后添加输入检查、输出审计、日志记录等横切逻辑。",
        agent=agent,
        model=agent.model,
        num_iterations=1,
        print_summary=False,
        print_results=False,
    )

    result = eval_case.run_with_output(
        output="Hooks 用来在模型运行前后加入校验、审计和日志等横切逻辑。",
        print_summary=False,
        print_results=False,
    )
    print("\n--- AccuracyEval 结果 ---")
    if result:
        print(f"平均分: {result.avg_score}")
        for item in result.results:
            print(f"score={item.score}, reason={item.reason}")


def measured_function() -> str:
    """PerformanceEval 使用的普通函数。"""
    return "Agno evals can measure quality and performance."


def run_performance_eval_demo() -> None:
    """场景二：用 PerformanceEval 评估函数性能。"""
    perf_eval = PerformanceEval(
        name="lesson_59_performance_eval",
        func=measured_function,
        warmup_runs=1,
        num_iterations=3,
        print_summary=False,
        print_results=False,
    )
    result = perf_eval.run(print_summary=False, print_results=False)
    print("\n--- PerformanceEval 结果 ---")
    if result:
        print(f"运行次数: {len(result.run_times)}")
        print(f"平均耗时: {result.avg_run_time:.6f}s")


def run_evals_basics_example() -> None:
    """演示 Agno 的 Evals 基础能力。"""
    run_accuracy_eval_demo()
    run_performance_eval_demo()

    print("\n--- 关键观察点 ---")
    print("1. AccuracyEval 适合用输入、期望输出和实际输出评估回答质量。")
    print("2. run_with_output 可以直接评估已有输出。")
    print("3. PerformanceEval 适合评估函数运行时长和资源表现。")
    print("4. Evals 是把学习示例推进到可回归验证的重要一步。")


if __name__ == "__main__":
    run_evals_basics_example()
