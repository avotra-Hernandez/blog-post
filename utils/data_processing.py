import pandas as pd
from glob import glob
import os


def read_csv(url_or_file):
    try:
        # Check if the URL is a Google Sheets link
        if "docs.google.com/spreadsheets" in url_or_file:
            # Read the file from the Google Sheets link
            df = pd.read_csv(url_or_file)

        # If it's not a Google Sheets link, assume it's a local file
        else:
            # Read the CSV file from a local file
            df = pd.read_csv(url_or_file)
        return df

    except pd.errors.EmptyDataError:
        print("The file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the CSV file.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def data_filtered(path_data, columns_used, renamed_columns, streamlit=False):
    df_filtered = pd.DataFrame()
    if not streamlit:
        all_csv = glob(os.path.join(path_data, "*.csv"))
    else:
        all_csv = [path_data]

    for csv in all_csv:
        df = pd.read_csv(csv)
        df_filtered = pd.concat([df_filtered, df])
    df_filtered = df[columns_used].rename(columns=renamed_columns)



    return df_filtered
