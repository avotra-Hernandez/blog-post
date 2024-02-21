from constant import MODEL_NAME_EMBEDDING, SECRET_KEY
from model_llm.model_chat_llm import model_llama_api
from model_llm.model_embedding import model_embedding

from utils.frontend import front

model_llm = model_llama_api(SECRET_KEY)
model_embedding = model_embedding(MODEL_NAME_EMBEDDING, 'cpu')
front(model_llm, model_embedding)