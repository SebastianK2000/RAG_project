import streamlit as st
from embeddings import EmbeddingModel
from vector_store import load_faiss_index
from retriever import search_similar_chunks
from qa import build_answer_from_chunks

st.title("Asystent Dokumentacji NAS Synology")

model = EmbeddingModel()
index, metadata = load_faiss_index("index/faiss_index.bin", "index/metadata.json")

query = st.text_input("Wpisz pytanie:")

if query:
    results = search_similar_chunks(
        query=query,
        embedding_model=model,
        index=index,
        metadata=metadata,
        top_k=3
    )
    answer = build_answer_from_chunks(query, results)
    
    st.subheader("Odpowiedź")
    st.write(answer)
    
    st.subheader("Źródła")
    for r in results:
        st.write(f"**{r['source']} | chunk {r['chunk_id']}**")
        st.write(r["text"])