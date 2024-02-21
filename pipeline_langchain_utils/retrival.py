from langchain.chains import RetrievalQA

def retrival(model_llm, vectordb):
    qa_chain = RetrievalQA.from_chain_type(
        model_llm,
        retriever=vectordb.as_retriever()
    )
    return qa_chain
