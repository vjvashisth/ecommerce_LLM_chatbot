import pandas as pd

def load_product_data(filepath):
    """
    Loads the product dataset from a CSV file and constructs a combined text field
    for each product by concatenating the title, features, and description.

    Args:
        filepath (str): Path to the CSV file containing product data.

    Returns:
        pd.DataFrame: DataFrame with an additional 'combined_text' column for embedding.
    """
    df = pd.read_csv(filepath)

    def combine(row):
        """
        Combines the title, features, and description fields of a product into a single text string.
        Uses eval() to convert stored stringified lists (e.g., "['Feature 1', 'Feature 2']") back to lists.

        Args:
            row (pd.Series): A row of the DataFrame representing a product.

        Returns:
            str: Combined string of title, features, and description.
        """
        title = row["title"]
        features = " ".join(eval(row["features"])) if isinstance(row["features"], str) and row["features"].startswith("[") else ""
        description = " ".join(eval(row["description"])) if isinstance(row["description"], str) and row["description"].startswith("[") else ""
        return f"{title}. {features} {description}"

    # Apply text combination for all rows
    df["combined_text"] = df.apply(combine, axis=1)

    return df
