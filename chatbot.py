from retriever import retrieve_top_k
from order_api import fetch_customer_orders

def classify_query(query):
    if "order" in query.lower() or "shipping" in query.lower() or "purchase" in query.lower():
        return "order"
    return "product"

def generate_response(query, embed_model, corpus_embeddings, corpus_texts, llm_func):
    query_type = classify_query(query)
    if query_type == "order":
        customer_id = ''.join(filter(str.isdigit, query))
        return fetch_customer_orders(int(customer_id))
    else:
        contexts = retrieve_top_k(query, corpus_embeddings, corpus_texts, embed_model)
        context_str = "\n".join([ctx[0] for ctx in contexts])
        return llm_func(query, context_str)