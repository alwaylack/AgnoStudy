from pathlib import Path


def generate_sample_pdf() -> None:
    """生成一个用于 PDF Reader 学习的示例 PDF。"""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        from reportlab.pdfgen import canvas
    except ImportError as exc:
        raise ImportError(
            "运行这个脚本前，请先安装 PDF 依赖：`uv pip install -U reportlab pypdf`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "output" / "pdf"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "agno_knowledge_sample.pdf"

    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))

    pdf = canvas.Canvas(str(output_path), pagesize=A4)
    pdf.setTitle("Agno Knowledge Sample")

    width, height = A4
    y = height - 60

    def write_line(text: str, font_size: int = 12, gap: int = 24) -> None:
        nonlocal y
        pdf.setFont("STSong-Light", font_size)
        pdf.drawString(50, y, text)
        y -= gap

    write_line("Agno PDF Reader 学习资料", font_size=18, gap=32)
    write_line("1. Knowledge 用来管理和检索外部资料。")
    write_line("2. Memory 更关注记住用户和会话上下文。")
    write_line("3. Tools 让 Agent 可以调用外部能力。")
    write_line("4. RAG 的常见流程是：导入资料、建立向量索引、检索、生成回答。")
    write_line("5. PDF Reader 适合把 PDF 文档接入 Knowledge。")

    pdf.showPage()
    y = height - 60

    write_line("Agno 学习建议", font_size=18, gap=32)
    write_line("1. 先掌握最小可运行示例。")
    write_line("2. 再学习 Tools、Memory 和 Knowledge。")
    write_line("3. 最后再做检索优化和多 Agent 协作。")

    pdf.save()
    print(output_path)


if __name__ == "__main__":
    generate_sample_pdf()
