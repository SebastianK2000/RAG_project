import re

def clean_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text, flags=re.UNICODE)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()