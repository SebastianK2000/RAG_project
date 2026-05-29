from pathlib import Path
from pypdf import PdfReader

def load_txt(file_path: Path) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf(file_path: Path) -> str:
    reader = PdfReader(str(file_path))
    text_parts = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_parts.append(page_text)
    return "\n".join(text_parts)

def load_documents(data_dir: str) -> list[dict]:
    documents = []
    data_path = Path(data_dir)
    for file_path in data_path.iterdir():
        if file_path.is_file():
            if file_path.suffix.lower() == ".txt":
                text = load_txt(file_path)
            elif file_path.suffix.lower() == ".pdf":
                text = load_pdf(file_path)
            else:
                continue
            documents.append({
                "source": file_path.name,
                "text": text
            })
    return documents