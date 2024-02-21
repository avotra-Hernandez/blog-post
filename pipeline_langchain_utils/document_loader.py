from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders import WebBaseLoader
import requests


def load_document(type_of_document, url_youtube=None, url_web=None, pdf_storage=None):
    docs = []

    if type_of_document == "pdf":
        loader = PyPDFLoader(pdf_storage)
        docs = loader.load()

    if type_of_document == "youtube":
        save_dir = "docs/youtube/"
        loader = GenericLoader(
            YoutubeAudioLoader([url_youtube], save_dir),
            OpenAIWhisperParser()
        )
        docs = loader.load()

    if type_of_document == "web":
        try:
            loader = WebBaseLoader(url_web)
            docs = loader.load()
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.ConnectTimeout:
            pass
    return docs