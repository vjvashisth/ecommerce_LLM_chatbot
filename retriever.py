from sklearn.metrics.pairwise import cosine_similarity

def retrieve_top_k(query, corpus_embeddings, corpus_texts, embed_model, k=3):
    query_embedding = embed_model.encode([query])
    similarities = cosine_similarity(query_embedding, corpus_embeddings)[0]
    top_k_idx = similarities.argsort()[-k:][::-1]
    return [(corpus_texts[i], similarities[i]) for i in top_k_idx]