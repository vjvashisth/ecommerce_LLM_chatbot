def dummy_llm(query, context):
    """
    Simulates a response from a language model using the query and provided context.

    Args:
        query (str): The user's input question.
        context (str): Retrieved product or order context relevant to the query.

    Returns:
        str: A simple templated response combining the query and context.
    """
    return f"Q: {query}\nBased on the following product info:\n{context}"

# ------------------ Optional: Use a real LLM (e.g., OpenAI GPT-3.5) ------------------
# Uncomment and configure the following if you want to use OpenAI's API instead
#
# import openai
# openai.api_key = "YOUR_API_KEY"
#
# def openai_llm(query, context):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful e-commerce assistant."},
#             {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
#         ]
#     )
#     return response['choices'][0]['message']['content']
#
# -------------------------------------------------------------------------------------
