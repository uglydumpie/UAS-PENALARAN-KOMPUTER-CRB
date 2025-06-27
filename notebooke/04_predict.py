# 04_predict.py
from collections import Counter
from 03_retrieval import retrieve  # asumsi retrieval.py ada

# contoh case_solutions dummy
case_solutions = {
    "case_001": "mengabulkan",
    "case_002": "menolak",
    "case_003": "menghukum"
}

def predict_outcome(query):
    top_k = retrieve(query, k=5)
    solusi = [case_solutions[c] for c in top_k if c in case_solutions]
    return Counter(solusi).most_common(1)[0][0]