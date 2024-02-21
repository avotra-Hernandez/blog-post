MAX_DEPTH = 2
COLUMNS_USED = ['firstName','currentCompanyName','linkedinProfileUrl','mailFromDropContact', 'currentJobTitle', 'websiteFromDropContact']
RENAMED_COLUMNS = {
    "firstName":"First Name",
    "currentCompanyName":"Company Name",
    "linkedinProfileUrl":"Linkedin URL",
    "mailFromDropContact":"email",
    "websiteFromDropContact":"Website"
}
PATH_DATA = "data/"
OUTPUT_PATH = "data_output/"
OUTPUT_FILE_NAME = "data_clean.csv"
MODEL_NAME = "TheBloke/Llama-2-13b-Chat-GPTQ"
MODEL_NAME_EMBEDDING = "thenlper/gte-large"
SECRET_KEY = "LL-A3A4JAwBD3a4Wwy30VlfdEPfhZ1uUVNhvcqGXUntlO7TA75Cvzr7NF6EidOCEsmV"

INDEX_WEBSITE = 5
INDEX_COMPANY_NAME = 1


MAX_NEW_TOKEN = 1024
TEMPERATURE = 0.0001
TOP_P = 0.95
REPETITION_PENALITY = 1.15

CHUNK_SIZE = 1024
CHUNK_OVERLAP = 64
#
# CHUNK_SIZE = 26
# CHUNK_OVERLAP = 4

