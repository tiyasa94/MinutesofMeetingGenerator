from embedding import get_text_embedding
from sklearn.neighbors import NearestNeighbors
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import Any
from chromadb.api.types import EmbeddingFunction
from chunking import text_to_chunks

# Load the model from TF Hub
class MiniLML6V2EmbeddingFunction(EmbeddingFunction):
    MODEL = SentenceTransformer('all-MiniLM-L6-v2')
    def __call__(self, texts):
        return MiniLML6V2EmbeddingFunction.MODEL.encode(texts).tolist()

def nearest_reference(question, text):
    print("Inside nearest neighbor function\n")
    chunks = text_to_chunks([text])
    emb_function = MiniLML6V2EmbeddingFunction()
    emb_question = emb_function([question])
    embeddings = get_text_embedding(chunks)

    nn = NearestNeighbors(n_neighbors=1)
    nn.fit(embeddings)

    neighbors = nn.kneighbors(emb_question, return_distance=False)
    neighbors

    topn_chunks = [chunks[i] for i in neighbors.tolist()[0]]
    return topn_chunks