def search_similar_chunks(query: str, embedding_model, index, metadata, top_k: int = 3, max_distance: float = 1.54):
    
    query_vector = embedding_model.encode([query]).astype("float32")
    distances, indices = index.search(query_vector, top_k)
    
    results = []
    for i, idx in enumerate(indices[0]):
        distance = distances[0][i]
        
        if idx < len(metadata) and distance < max_distance:
            results.append(metadata[idx])
            
    return results