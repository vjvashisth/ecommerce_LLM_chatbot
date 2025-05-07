import pandas as pd

def load_product_data(filepath):
    df = pd.read_csv(filepath)
    def combine(row):
        title = row["title"]
        features = " ".join(eval(row["features"])) if isinstance(row["features"], str) and row["features"].startswith("[") else ""
        description = " ".join(eval(row["description"])) if isinstance(row["description"], str) and row["description"].startswith("[") else ""
        return f"{title}. {features} {description}"
    df["combined_text"] = df.apply(combine, axis=1)
    return df