from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI


def model_llama_api(secret_key):
    llm = LlamaAPI(secret_key)
    model_llm = ChatLlamaAPI(client=llm)
    return model_llm