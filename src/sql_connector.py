"""
This file is responsible for handing the SQL db connection
"""

import os 
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv

def create_engine():

    load_dotenv()
    connection_url = URL.create(
        "mssql+pyodbc",
        host=os.getenv("SERVER"),
        database=os.getenv("DATABASE"),
        query={
            "driver": "ODBC Driver 18 for SQL Server",
            "Trusted_Connection": "yes",
            "TrustedServerCertificate": "yes",
        },
    )

    engine = create_engine(connection_url)
    return engine
