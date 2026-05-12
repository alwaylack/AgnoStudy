"""Multimodal 基础示例。

演示 Agno 的 Multimodal 能力，包括：
1. 构建 Image / File 等媒体输入对象
2. 在 Agent.run 中传入 images / files
3. 用 send_media_to_model 控制是否发送媒体给模型
4. 明确多模态能力依赖底层模型支持

默认运行只演示媒体对象和传参方式，不调用模型。
如需观察真实模型调用，可设置 RUN_MULTIMODAL_LIVE=1。
"""

import os
import sys
from pathlib import Path

from agno.media import File, Image

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models import OpenAIModel


def build_sample_markdown_file() -> File:
    """把本地学习进度文档作为 File 输入。"""
    progress_path = PROJECT_ROOT / "contexts" / "learning_progress.md"
    return File(
        filepath=str(progress_path),
        mime_type="text/markdown",
        filename="learning_progress.md",
    )


def build_reference_image() -> Image:
    """构建一个远程图片对象，用来演示图片输入形态。"""
    return Image(
        url="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        alt_text="A placeholder image used to demonstrate multimodal image input.",
    )


def describe_media_inputs() -> None:
    """默认场景：只构建媒体对象，避免被具体模型的多模态兼容性卡住。"""
    sample_file = build_sample_markdown_file()
    reference_image = build_reference_image()

    print("\n--- File 输入对象 ---")
    print(f"filename: {sample_file.filename}")
    print(f"filepath: {sample_file.filepath}")
    print(f"mime_type: {sample_file.mime_type}")

    print("\n--- Image 输入对象 ---")
    print(f"url: {reference_image.url}")
    print(f"alt_text: {reference_image.alt_text}")

    print("\n--- Agent.run 传参形态 ---")
    print("agent.run('请阅读附件', files=[sample_file], ...)")
    print("agent.run('请描述图片', images=[reference_image], ...)")


def run_file_input_demo(model: OpenAIModel) -> None:
    """场景一：传入文件，让模型读取学习进度。"""
    agent = model.create_agent(
        name="Multimodal File Agent",
        instructions=[
            "你是 Agno Multimodal 示例的学习助教。",
            "如果收到了文件，请基于文件内容总结当前学习进度。",
        ],
        markdown=True,
        send_media_to_model=True,
    )

    try:
        response = agent.run(
            "请阅读我附带的学习进度文件，总结最近完成的三节课。",
            files=[build_sample_markdown_file()],
            user_id="student@example.com",
            session_id="lesson_56_file_input_demo",
        )
        print("\n--- 文件输入响应 ---")
        print(response.content)
    except Exception as exc:
        print("\n--- 文件输入调用失败 ---")
        print(type(exc).__name__)
        print(exc)
        print("当前模型服务可能不支持 Agno 发送的 file 消息格式。")


def run_image_input_demo(model: OpenAIModel) -> None:
    """场景二：传入图片对象，说明模型需支持视觉输入。"""
    agent = model.create_agent(
        name="Multimodal Image Agent",
        instructions=[
            "你是 Agno Multimodal 示例的学习助教。",
            "请说明你是否能使用图片内容，并给出保守回答。",
        ],
        markdown=True,
        send_media_to_model=True,
    )

    try:
        response = agent.run(
            "请描述这张图片，并说明在 Agno 中图片是如何作为输入传入的。",
            images=[build_reference_image()],
            user_id="student@example.com",
            session_id="lesson_56_image_input_demo",
        )
        print("\n--- 图片输入响应 ---")
        print(response.content)
    except Exception as exc:
        print("\n--- 图片输入调用失败 ---")
        print(type(exc).__name__)
        print(exc)
        print("当前模型服务可能不支持 Agno 发送的 image 消息格式。")


def run_multimodal_basics_example() -> None:
    """演示 Agno 的 Multimodal 基础能力。"""
    describe_media_inputs()

    if os.getenv("RUN_MULTIMODAL_LIVE") == "1":
        model = OpenAIModel.from_env()
        run_file_input_demo(model)
        run_image_input_demo(model)
    else:
        print("\n--- 模型调用默认跳过 ---")
        print("设置 RUN_MULTIMODAL_LIVE=1 后，本脚本会把 File / Image 真实发送给模型。")

    print("\n--- 关键观察点 ---")
    print("1. Agno 用 Image / Audio / Video / File 等对象表达多模态输入。")
    print("2. Agent.run 可以通过 images / files 等参数传入媒体。")
    print("3. send_media_to_model 控制是否把媒体发送给底层模型。")
    print("4. 实际效果取决于所选模型是否支持对应模态。")


if __name__ == "__main__":
    run_multimodal_basics_example()
