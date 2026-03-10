import faiss
import numpy as np

dimension = 3

index = faiss.IndexFlatL2(dimension)

transaction_vectors = np.array([
    [2000, 1, 1],
    [4500, 1, 0],
    [5000, 1, 1]
]).astype("float32")

index.add(transaction_vectors)

query = np.array([[4700, 1, 1]]).astype("float32")

distances, indices = index.search(query, k=2)

print(indices)