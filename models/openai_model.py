import os
from typing import Any

from agno.agent import Agent
from agno.models.openai.like import OpenAILike
from dotenv import load_dotenv

load_dotenv()


class OpenAIModel:
    """封装兼容 OpenAI 的模型，方便在不同的 Agno 示例中复用。"""

    def __init__(
        self,
        model_id: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        **model_kwargs: Any,
    ) -> None:
        self.model_id = model_id or os.getenv("OPENAI_MODEL_ID")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")
        # 透传更多模型参数，便于后续学习 temperature、max_tokens 等配置。
        self.model_kwargs = model_kwargs
        self._validate_config()

    def _validate_config(self) -> None:
        missing = []
        if not self.model_id:
            missing.append("OPENAI_MODEL_ID")
        if not self.api_key:
            missing.append("OPENAI_API_KEY")
        if not self.base_url:
            missing.append("OPENAI_BASE_URL")

        if missing:
            raise ValueError(f"缺少模型配置: {', '.join(missing)}")

    def get_model(self) -> OpenAILike:
        """根据当前配置构建 Agno 的 OpenAILike 模型实例。"""
        return OpenAILike(
            id=self.model_id,
            api_key=self.api_key,
            base_url=self.base_url,
            **self.model_kwargs,
        )

    def create_agent(self, name: str = "Agno Agent", **kwargs: Any) -> Agent:
        """创建一个使用当前模型的 Agno Agent。"""
        return Agent(name=name, model=self.get_model(), **kwargs)

    def print_response(self, message: str, **agent_kwargs: Any) -> None:
        """直接打印一次响应，适合用来快速做实验。"""
        agent = self.create_agent(markdown=True, **agent_kwargs)
        agent.print_response(message)

    def run(self, message: str, **agent_kwargs: Any) -> Any:
        """返回 Agent 的响应内容，便于调用方继续处理。"""
        agent = self.create_agent(**agent_kwargs)
        return agent.run(message)

    @classmethod
    def from_env(cls, **model_kwargs: Any) -> "OpenAIModel":
        """从环境变量创建默认的模型封装实例。"""
        return cls(**model_kwargs)

    @classmethod
    def quick_chat(cls, message: str, **agent_kwargs: Any) -> None:
        """单次快速对话的便捷入口。"""
        cls.from_env().print_response(message, **agent_kwargs)
