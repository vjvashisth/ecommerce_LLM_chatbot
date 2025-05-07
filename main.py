from data_loader import load_product_data
from embedder import generate_embeddings
from chatbot import generate_response
from llm_stub import dummy_llm

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown

# Console for rich output
console = Console()

# Load and embed data
product_df = load_product_data("data/Product_Information_Dataset.csv")
texts = product_df["combined_text"].tolist()
embeddings, model = generate_embeddings(texts)

# Header
console.print("[bold cyan]\nWelcome to the E-commerce Chatbot![/bold cyan]")
console.print("Ask about [green]products[/green] or your [magenta]orders[/magenta]. Type '[bold red]exit[/bold red]' to quit.\n")

# Chat loop
while True:
    user_input = console.input("[bold yellow]You[/bold yellow]: ")
    if user_input.lower() == "exit":
        console.print("\n[bold green]Thank you for using the assistant. Goodbye![/bold green]")
        break

    # Generate response
    response = generate_response(user_input, model, embeddings, texts, dummy_llm)

    # Display response with formatting
    if isinstance(response, str):
        console.print(Panel.fit(response, title="[bold green]Chatbot", border_style="cyan"))
    elif isinstance(response, list):
        console.print(f"\n[bold cyan]Found {len(response)} orders:[/bold cyan]\n")
        for order in response:
            summary = "\n".join([f"[bold]{k}[/bold]: {v}" for k, v in order.items()])
            console.print(Panel(summary, border_style="magenta"))
    else:
        console.print(f"[red]Unexpected response format:[/red] {response}")
