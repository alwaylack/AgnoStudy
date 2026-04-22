from pathlib import Path


# 基于项目根目录统一管理示例里会用到的路径。
PROJECT_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge_docs"
TMP_DIR = PROJECT_ROOT / "tmp"

# 这一课复用前面已经整理过的几份学习资料。
KNOWLEDGE_FILES = [
    KNOWLEDGE_DIR / "agno_rag_basics.md",
    KNOWLEDGE_DIR / "agno_tools_notes.md",
    KNOWLEDGE_DIR / "agno_memory_notes.md",
    KNOWLEDGE_DIR / "agno_beginner_track.md",
    KNOWLEDGE_DIR / "agno_advanced_track.md",
]
