from sentence_transformers import SentenceTransformer

def generate_embeddings(texts, model_name="all-MiniLM-L6-v2"):
    """
    Generates sentence embeddings for a list of input texts using a specified 
    SentenceTransformer model.

    Args:
        texts (List[str]): A list of strings to be embedded.
        model_name (str): Name of the pretrained SentenceTransformer model to use.
                          Default is "all-MiniLM-L6-v2".

    Returns:
        tuple:
            - embeddings (np.ndarray): Array of vector embeddings.
            - model (SentenceTransformer): The loaded SentenceTransformer model.
    """
    # Load the specified sentence transformer model
    model = SentenceTransformer(model_name)

    # Generate vector embeddings for the input texts
    embeddings = model.encode(texts, show_progress_bar=True)

    return embeddings, model
