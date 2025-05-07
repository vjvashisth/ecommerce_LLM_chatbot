from retriever import retrieve_top_k
from order_api import fetch_customer_orders

def classify_query(query):
    """
    Classifies the user query as either related to an 'order' or a 'product'.

    Args:
        query (str): The user's input query.

    Returns:
        str: 'order' if query is about shipping/order/purchase; otherwise 'product'.
    """
    if "order" in query.lower() or "shipping" in query.lower() or "purchase" in query.lower():
        return "order"
    return "product"

def generate_response(query, embed_model, corpus_embeddings, corpus_texts, llm_func):
    """
    Generates a chatbot response based on the user query type.

    Args:
        query (str): The user's question or request.
        embed_model (SentenceTransformer): The model used for embedding the query.
        corpus_embeddings (List[List[float]]): Precomputed embeddings of product texts.
        corpus_texts (List[str]): List of product-related texts.
        llm_func (Callable): Function to generate response using LLM (or dummy function).

    Returns:
        str or dict: Response text from LLM or customer order data from API.
    """
    query_type = classify_query(query)

    if query_type == "order":
        # Extract numeric part from query to guess customer ID
        customer_id = ''.join(filter(str.isdigit, query))
        return fetch_customer_orders(int(customer_id))
    
    else:
        # Retrieve top-k relevant product texts
        contexts = retrieve_top_k(query, corpus_embeddings, corpus_texts, embed_model)
        context_str = "\n".join([ctx[0] for ctx in contexts])

        # Generate a response using provided LLM function
        return llm_func(query, context_str)
