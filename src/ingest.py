"""
This file is responsible for ingesting a file into the database by using our engine object
"""

def write_to_sql(df, table_name, engine):

    try:
        df.to_sql(
            table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

    except Exception as e:
        print(f"Failed to import file {table_name}: {e}")