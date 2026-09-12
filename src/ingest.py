"""
This file is responsible for ingesting a file into the database by calling our SQL session object from our SQL connection file
"""

def ingest_file(file):
    if file.suffix == ".csv":
        print("")
    elif file.suffix == ".xlsx":
        print("")