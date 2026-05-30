import pandas as pd
import pickle
import os

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv(
    "/Users/prerana/Documents/AI_Shopping_Assistant/data/amazon_products.csv"
)

# Clean data
df = df.dropna(subset=["TITLE"])

df["DESCRIPTION"] = df["DESCRIPTION"].fillna("")
df["BULLET_POINTS"] = df["BULLET_POINTS"].fillna("")

# Combine text fields
df["combined_text"] = (
    df["TITLE"] + " " +
    df["DESCRIPTION"] + " " +
    df["BULLET_POINTS"]
)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Cache embeddings
if os.path.exists("embeddings.pkl"):

    with open("embeddings.pkl", "rb") as f:
        embeddings = pickle.load(f)

else:

    embeddings = model.encode(
        df["combined_text"].tolist(),
        show_progress_bar=True
    )

    with open("embeddings.pkl", "wb") as f:
        pickle.dump(embeddings, f)

def recommend_products(query, top_n=5):

    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    top_indices = similarities.argsort()[-top_n:][::-1]

    results = []

    for idx in top_indices:

        score = round(similarities[idx] * 100, 1)

        results.append({
            "title": df.iloc[idx]["TITLE"],
            "description": str(
                df.iloc[idx]["DESCRIPTION"]
            )[:300],
            "product_type": df.iloc[idx]["PRODUCT_TYPE_ID"],
            "length": df.iloc[idx]["PRODUCT_LENGTH"],
            "score": score
        })

    return results