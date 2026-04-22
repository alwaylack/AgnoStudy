def estimate_stage_difficulty(stage_name: str) -> str:
    """根据学习阶段返回一个简洁的难度说明。"""
    stage = stage_name.lower()
    difficulty_map = {
        "agent": "基础阶段，重点是先跑通最小 Agent 示例。",
        "tools": "基础到中等，适合在掌握 Agent 后继续学习。",
        "knowledge": "中等，建议先理解检索增强的基本流程。",
        "rag": "中等到进阶，重点在检索策略和上下文组织。",
        "team": "中等到进阶，适合在单 Agent 和 Knowledge 基础上继续。",
        "workflow": "进阶，重点在把多个步骤串成稳定流程。",
    }
    return difficulty_map.get(
        stage,
        f"{stage_name} 建议先从最小可运行示例开始，再逐步扩展复杂度。",
    )


def suggest_next_lesson(current_topic: str) -> str:
    """根据当前主题给出下一课建议。"""
    topic = current_topic.lower()
    if "team" in topic and "knowledge" in topic:
        return "下一步建议学习 Workflow，让多 Agent 协作进入可编排流程。"
    if "integrated" in topic or "project" in topic:
        return "下一步建议把项目骨架继续升级为 Workflow 风格的小应用。"
    if "rag" in topic:
        return "下一步建议把 RAG 和 Team 串起来，观察协作式检索。"
    return "下一步建议继续沿主线推进，并保持每节课都最小可运行。"
