from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI
from langchain.embeddings import HuggingFaceEmbeddings

from constant import MODEL_NAME_EMBEDDING
from model_llm.model_embedding import model_embedding
from pipeline_langchain_utils.document_loader import load_document
from pipeline_langchain_utils.document_splitting import text_splitting
from pipeline_langchain_utils.retrival import retrival
from pipeline_langchain_utils.vectorstore import vector_stores

def full_pipline(type_of_document, model_llm, model_embeding, url_web=None):
    qa_chain = []
    docs = load_document(type_of_document, url_web=url_web)
    if docs:
        docs = text_splitting(docs)
        vectordb = vector_stores(docs, model_embeding)
        qa_chain = retrival(model_llm, vectordb)
    return qa_chain