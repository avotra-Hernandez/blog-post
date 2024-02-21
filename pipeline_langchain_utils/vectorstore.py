from langchain.vectorstores import Chroma

def vector_stores(docs, model_embedding, persist_directory=None):
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=model_embedding,
        persist_directory=persist_directory
    )
    return vectordb