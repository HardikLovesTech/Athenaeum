from sentence_transformers import SentenceTransformer

EmbeddingModel = SentenceTransformer("all-miniLM-L6-v2")

def GenerateEmbedding(Text: str) -> list[float]:
    Embedding = EmbeddingModel.encode(
        Text,
        normalize_embeddings=True,
    )


    return Embedding.tolist()