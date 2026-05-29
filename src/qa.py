def build_answer_from_chunks(query: str, retrieved_chunks: list[dict]) -> str:
    if not retrieved_chunks:
        return "Nie znaleziono informacji w dokumentacji."
        
    answer = "Na podstawie znalezionych fragmentów dokumentacji:\n\n"
    for i, chunk in enumerate(retrieved_chunks, start=1):
        answer += f"[Źródło {i}: {chunk['source']} | chunk {chunk['chunk_id']}]\n"
        answer += chunk["text"] + "\n\n"
        
    return answer