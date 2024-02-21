from constant import RENAMED_COLUMNS, COLUMNS_USED
from model_llm.model_embedding import model_embedding
from utils.company_ckeck import company_check
from utils.data_processing import data_filtered
import streamlit as st
import tempfile


def front(model_llm, model_embedding):
    st.title("Check Company Name")

    menu = ["DocumentFiles"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        doc = st.file_uploader("Upload File", type=['txt', 'docx', 'pdf', "csv"])

        if st.button("Process"):
            if doc is not None:
                file_details = {"Filename": doc.name, "FileType": doc.type, "FileSize": doc.size}
                st.write(file_details)

                # Check File Type
                if doc.type == "text/csv":

                    data = data_filtered(doc, COLUMNS_USED, RENAMED_COLUMNS, streamlit=True)
                    data = company_check(data, model_llm, model_embedding)

                    st.write("Fichier traiter:")
                    st.write(data)

                    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
                        temp_file_name = temp_file.name
                        data.to_csv(temp_file_name + ".csv")
                    with open(temp_file_name + ".csv") as f:
                        st.download_button('Download CSV', f)
