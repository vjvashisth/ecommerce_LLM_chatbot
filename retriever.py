from sklearn.metrics.pairwise import cosine_similarity

def retrieve_top_k(query, corpus_embeddings, corpus_texts, embed_model, k=3):
    """
    Retrieves the top-k most relevant product texts based on similarity to the user query.

    This function embeds the query using the same model used to embed the product corpus,
    computes cosine similarities between the query and all corpus embeddings, and returns
    the top-k matches.

    Args:
        query (str): The user input query string.
        corpus_embeddings (np.ndarray): Precomputed embeddings for all product texts.
        corpus_texts (List[str]): The original text entries corresponding to each embedding.
        embed_model (SentenceTransformer): The model used to encode the query.
        k (int): The number of top results to return. Default is 3.

    Returns:
        List[Tuple[str, float]]: A list of tuples containing the top-k text entries and their similarity scores.
    
    Example:
        >>> retrieve_top_k("wireless microphone", embeddings, texts, model)
        [("BONAOK Wireless Bluetooth Karaoke Mic...", 0.89), ...]
    """
    # Generate embedding for the user query
    query_embedding = embed_model.encode([query])

    # Compute cosine similarities between query and all corpus entries
    similarities = cosine_similarity(query_embedding, corpus_embeddings)[0]

    # Identify indices of top-k highest similarity scores
    top_k_idx = similarities.argsort()[-k:][::-1]

    # Return the top-k matching texts and their scores
    return [(corpus_texts[i], similarities[i]) for i in top_k_idx]
