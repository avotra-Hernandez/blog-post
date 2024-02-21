from flask import Flask
from constant import RENAMED_COLUMNS, COLUMNS_USED, PATH_DATA, MODEL_NAME_EMBEDDING, MODEL_NAME, OUTPUT_PATH, \
    OUTPUT_FILE_NAME

from utils.check_company import check_all_company
from utils.data_processing import data_filtered
from langchain.embeddings import HuggingFaceEmbeddings
import os

from utils.nlp import llama_api
app = Flask(__name__)

@app.route('/api/marketing', methods=['GET'])
def check_company_result():
    # load and transform data
    data = data_filtered(PATH_DATA, COLUMNS_USED, RENAMED_COLUMNS)
    print("data loaded ...")
    llm = llama_api("LL-A3A4JAwBD3a4Wwy30VlfdEPfhZ1uUVNhvcqGXUntlO7TA75Cvzr7NF6EidOCEsmV")
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME_EMBEDDING,
                                       model_kwargs={"device": "cuda"},
                                       encode_kwargs={"normalize_embeddings": True})
    print("FH pipeline done ...")

    # Langchain
    data = check_all_company(data, embeddings, llm)

    # Write
    data.to_csv(os.path.join(OUTPUT_PATH, OUTPUT_FILE_NAME))


@app.route('/api/hello', methods=['GET'])
def hello():
    return {'message': 2+2+2}

if __name__ == '__main__':
    app.run(debug=True)