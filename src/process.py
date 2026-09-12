"""
This file is responsible for processing the files based on their extension and calling the write_to_sql function on the file
"""

from src.ingest import write_to_sql

def process_file(file):
    if file.suffix == ".csv":
        with open(file, "r") as f:
            write_to_sql(f)
    elif file.suffix == ".xlsx":
        print("")