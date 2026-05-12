"""Guardrails 基础示例。

演示 Agno 的 Guardrails 能力，包括：
1. 使用内置 PIIDetectionGuardrail
2. 阻止含 PII 的输入
3. mask_pii=True 时修改输入而不是抛错
4. 区分 Guardrails 与普通 Hooks

默认运行只演示 guardrail 本身，不调用模型。
如需观察 Agent 集成效果，可设置 RUN_GUARDRAILS_LIVE=1。
"""

import os
import sys
from pathlib import Path

from agno.exceptions import InputCheckError
from agno.guardrails import PIIDetectionGuardrail
from agno.run.agent import RunInput

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models import OpenAIModel


def run_blocking_guardrail_demo() -> None:
    """场景一：检测到 PII 后阻止继续执行。"""
    guardrail = PIIDetectionGuardrail(mask_pii=False)
    run_input = RunInput(input_content="我的邮箱是 student@example.com，请记住它。")

    try:
        guardrail.check(run_input)
    except InputCheckError as exc:
        print("\n--- Guardrail 拦截结果 ---")
        print(exc.message)
        print(exc.additional_data)
        print("这是本场景的预期结果：检测到 PII 后，输入不会继续进入模型。")


def run_masking_guardrail_demo() -> None:
    """场景二：检测到 PII 后先脱敏再继续。"""
    guardrail = PIIDetectionGuardrail(mask_pii=True)
    run_input = RunInput(input_content="我的电话是 138-123-4567，请解释为什么不要把它直接发给模型。")

    print("\n--- 脱敏前输入 ---")
    print(run_input.input_content)
    guardrail.check(run_input)
    print("\n--- 脱敏后输入 ---")
    print(run_input.input_content)


def run_agent_guardrail_live_demo() -> None:
    """可选场景：把 guardrail 挂到 Agent pre_hooks 上。"""
    model = OpenAIModel.from_env()
    agent = model.create_agent(
        name="Masking Guardrail Agent",
        pre_hooks=[PIIDetectionGuardrail(mask_pii=True)],
        instructions=[
            "你是 Guardrails 示例助教。",
            "请说明你收到的信息是否已经被脱敏。",
        ],
        markdown=True,
    )

    response = agent.run(
        "我的电话是 138-123-4567，请解释为什么不要把它直接发给模型。",
        user_id="student@example.com",
        session_id="lesson_57_masking_guardrail_demo",
    )
    print("\n--- Agent 集成响应 ---")
    print(response.content)


def run_guardrails_basics_example() -> None:
    """演示 Agno 的 Guardrails 基础能力。"""
    run_blocking_guardrail_demo()
    run_masking_guardrail_demo()

    if os.getenv("RUN_GUARDRAILS_LIVE") == "1":
        run_agent_guardrail_live_demo()
    else:
        print("\n--- Agent 集成默认跳过 ---")
        print("设置 RUN_GUARDRAILS_LIVE=1 后，会把 guardrail 挂到 Agent pre_hooks 并调用模型。")

    print("\n--- 关键观察点 ---")
    print("1. Guardrails 是更结构化的安全/质量检查，通常挂在 pre_hooks 或 post_hooks。")
    print("2. PIIDetectionGuardrail 可以阻止或脱敏邮箱、电话、信用卡等 PII。")
    print("3. 抛出 InputCheckError 可以在模型调用前终止运行。")
    print("4. Hooks 更通用，Guardrails 更适合安全策略和合规边界。")


if __name__ == "__main__":
    run_guardrails_basics_example()
