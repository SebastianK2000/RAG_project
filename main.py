from src.loaders import load_documents
from src.preprocessing import clean_text
from src.chunking import build_chunks
from src.embeddings import EmbeddingModel
from src.vector_store import build_faiss_index, save_faiss_index

def main():
    print("Wczytywanie dokumentów z data/raw...")
    documents = load_documents("data/raw")
    
    print("Czyszczenie tekstu...")
    for doc in documents:
        doc["text"] = clean_text(doc["text"])
        
    print("Dzielenie na chunki...")
    chunks = build_chunks(documents, chunk_size=800, overlap=100)
    
    print("Inicjalizacja modelu AI...")
    model = EmbeddingModel()
    
    print("Tworzenie embeddingów (to potrwa chwilę)...")
    texts = [chunk["text"] for chunk in chunks]
    vectors = model.encode(texts)
    
    print("Budowa i zapis bazy FAISS...")
    index = build_faiss_index(vectors)
    save_faiss_index(
        index=index,
        metadata=chunks,
        index_path="index/faiss_index.bin",
        metadata_path="index/metadata.json"
    )
    
    print("\nSUKCES! Indeks został zbudowany poprawnie.")
    print(f"Liczba dokumentów: {len(documents)}")
    print(f"Liczba chunków: {len(chunks)}")

if __name__ == "__main__":
    main()