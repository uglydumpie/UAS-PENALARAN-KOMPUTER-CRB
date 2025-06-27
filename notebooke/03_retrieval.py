# 03_retrieval.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/processed/cases.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["ringkasan_fakta"].fillna(""))

def retrieve(query, k=5):
    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, X).flatten()
    top_k_idx = sims.argsort()[-k:][::-1]
    return df.iloc[top_k_idx]["case_id"].tolist()