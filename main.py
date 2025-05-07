from data_loader import load_product_data
from embedder import generate_embeddings
from chatbot import generate_response
from llm_stub import dummy_llm

product_df = load_product_data("data/Product_Information_Dataset.csv")
texts = product_df["combined_text"].tolist()
embeddings, model = generate_embeddings(texts)

print("Welcome to the E-commerce Chatbot. Ask a question (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = generate_response(user_input, model, embeddings, texts, dummy_llm)
    print("Bot:", response)