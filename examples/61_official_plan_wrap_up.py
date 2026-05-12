"""官方课程计划收尾示例。

这一课不是新 API，而是把当前仓库课程和 Agno SDK Introduction 的主线做一次收束：
1. 检查已补齐的 Advanced / Production 课程文件
2. 打印下一步产品化整理建议
3. 为回到 study_assistant_app 做准备
"""

from pathlib import Path


COURSE_FILES = [
    "49_context_management_basics.py",
    "50_state_management_basics.py",
    "51_chat_history_basics.py",
    "52_dependency_injection_basics.py",
    "53_hooks_basics.py",
    "54_skills_basics.py",
    "55_reasoning_basics.py",
    "56_multimodal_basics.py",
    "57_guardrails_basics.py",
    "58_human_in_the_loop_basics.py",
    "59_evals_basics.py",
    "60_tracing_basics.py",
    "62_context_compression_basics.py",
    "63_run_cancellation_basics.py",
    "64_background_execution_basics.py",
    "65_mcp_basics.py",
    "66_product_app_capabilities.py",
]


def run_official_plan_wrap_up_example() -> None:
    """打印官方计划对齐结果。"""
    examples_dir = Path(__file__).resolve().parent

    print("\n--- 官方计划对齐检查 ---")
    missing = []
    for file_name in COURSE_FILES:
        exists = (examples_dir / file_name).exists()
        print(f"{'OK' if exists else 'MISSING'} - {file_name}")
        if not exists:
            missing.append(file_name)

    print("\n--- 当前结论 ---")
    if missing:
        print(f"还有 {len(missing)} 个课程文件缺失: {missing}")
    else:
        print("Advanced / Production 对齐补课线已经补齐到当前 SDK Introduction 的主线。")

    print("\n--- 下一步建议 ---")
    print("1. 回到 study_assistant_app，把 Skills / Guardrails / Tracing 纳入产品入口。")
    print("2. 为关键课程脚本补最小 smoke test，避免 Agno 版本升级后接口漂移。")
    print("3. 将 docs/learning_handbook.md 整理成完整学习手册。")


if __name__ == "__main__":
    run_official_plan_wrap_up_example()
