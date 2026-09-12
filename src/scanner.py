"""
This file is responsible for scanning all the files inside the given directory.
"""

from src.process import process_file

def scan_files(source_path):

    files = source_path.iterdir()
    # files = source_path.glob('*.csv') # use this to only grab certain file types
    for file in files:
        if file.is_file():
            process_file(file)