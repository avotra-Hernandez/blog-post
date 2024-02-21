from langchain.embeddings import HuggingFaceEmbeddings


def model_embedding(name_embedding, device_type):
    embedding_model = HuggingFaceEmbeddings(model_name=name_embedding, model_kwargs={"device": device_type},
                                            encode_kwargs={"normalize_embeddings": True})
    return embedding_model
