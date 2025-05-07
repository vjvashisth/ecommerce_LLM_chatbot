# E-commerce Assistant Chatbot

This project implements a modular Retrieval-Augmented Generation (RAG) chatbot for answering queries about products and orders from an e-commerce dataset.

## 🔧 Features

- **Product Q&A**: Uses sentence-transformer embeddings and vector search to retrieve product info.
- **Order Lookup**: Calls a local FastAPI service to retrieve customer order data.
- **LLM Integration**: Uses a dummy local function (`llm_stub.py`) for simulation (can be replaced with OpenAI/HuggingFace).
- **Modular Design**: Clean separation between embedding, retrieval, API, and chatbot logic.

## 🗂️ Project Structure

```
ecommerce_chatbot_solution/
├── chatbot.py            # Core logic to classify queries and generate responses
├── data_loader.py        # Load and preprocess product data
├── embedder.py           # Sentence embedding generation using transformers
├── llm_stub.py           # Simulated LLM function
├── main.py               # CLI runner for the chatbot
├── order_api.py          # Order API caller (uses HTTP to interact with FastAPI)
├── retriever.py          # Vector-based similarity search
├── README.md             # This file
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vjvashisth/ecommerce_LLM_chatbot.git
cd ecommerce_LLM_chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI server (in a new terminal)

```bash
uvicorn mock_api:app --reload
```

Ensure `Order_Data_Dataset.csv` is accessible at the root or change the path in `mock_api.py`.

### 4. Run the chatbot

```bash
python main.py
```

## ✅ Example Queries

- "Tell me about the best microphones under $30"
- "What did customer 37077 order last year?"
- "Suggest guitar accessories"
- "Find car media players"
- "Where's my order, customer 41066?"

## 📦 Dependencies

- `sentence-transformers`
- `scikit-learn`
- `pandas`
- `uvicorn`
- `fastapi`
- `requests`

## 🧠 Replace LLM

To use a real LLM, replace `dummy_llm` in `llm_stub.py` with OpenAI or HuggingFace code.

---

Built with ❤️ for GenAI.Labs challenge.
