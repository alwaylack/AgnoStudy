import os

from agno.knowledge.embedder.openai_like import OpenAILikeEmbedder
from dotenv import load_dotenv

load_dotenv()


class OpenAICompatibleEmbedder:
    """封装兼容 OpenAI 的嵌入模型，方便在 Knowledge 示例中复用。"""

    def __init__(
        self,
        model_id: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        dimensions: int | None = None,
    ) -> None:
        self.model_id = model_id or os.getenv("OPENAI_EMBEDDING_MODEL_ID")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")
        self.dimensions = dimensions or self._read_dimensions()
        self._validate_config()

    def _read_dimensions(self) -> int:
        raw_value = os.getenv("OPENAI_EMBEDDING_DIMENSIONS", "1536")
        try:
            return int(raw_value)
        except ValueError as exc:
            raise ValueError("OPENAI_EMBEDDING_DIMENSIONS 必须是整数。") from exc

    def _validate_config(self) -> None:
        missing = []
        if not self.model_id:
            missing.append("OPENAI_EMBEDDING_MODEL_ID")
        if not self.api_key:
            missing.append("OPENAI_API_KEY")
        if not self.base_url:
            missing.append("OPENAI_BASE_URL")

        if missing:
            raise ValueError(f"缺少嵌入模型配置: {', '.join(missing)}")

    def get_embedder(self) -> OpenAILikeEmbedder:
        """根据当前配置创建 OpenAI 兼容嵌入器。"""
        return OpenAILikeEmbedder(
            id=self.model_id,
            api_key=self.api_key,
            base_url=self.base_url,
            dimensions=self.dimensions,
        )

    @classmethod
    def from_env(cls) -> "OpenAICompatibleEmbedder":
        """从环境变量创建默认嵌入器配置。"""
        return cls()
