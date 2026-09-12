"""
This file is responsible for processing the files based on their extension and calling the write_to_sql function on the file
"""

from src.ingest import write_to_sql
import pandas as pd


def process_file(file, engine):
    if file.suffix == ".csv":
        df = pd.read_csv(file)
        file_name = file.stem
        write_to_sql(df, file_name, engine)
    elif file.suffix == ".xlsx":
        print("Excel processing not implemented yet.")
    else:
        print("Unexpected file type.")