"""
This file acts as my orchestration file.
This app should be run via the CLI using the python main.py "<path/to/folder>" command
"""

import sys
from pathlib import Path
from src.scanner import scan_files
from src.sql_connector import create_engine

def main():

    input_folder = Path(sys.argv[1]) # assuming we run python main.py "<path/to/folder>", this returns <path/to/folder> as a Path object.

    if not input_folder.exists():
        print("This folder path does not exist")
        return
    if not input_folder.is_dir():
        print("This is not a directory, did you try to pass a file by mistake?")
        return

    # Orchestration
    engine = create_engine()
    scan_files(input_folder, engine)
    # enforce_schema() - optional
    # import_files()

# this makes sure that we only run main() when we are in the root directory. Otherwise, we can safely import stuff from this file elsewhere without running main
if __name__ == "__main__":
    main()
    

