from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from constant import CHUNK_SIZE, CHUNK_OVERLAP


def text_splitting(docs):
    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return r_splitter.split_documents(docs)