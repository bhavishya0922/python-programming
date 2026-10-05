"""
Problem: Automated Directory Cleaning and Extension Sorter
Author: Bhavishya Dewangan
"""
import os
import shutil
from pathlib import Path

def categorize_files(directory: str):
    """Sorts files into subdirectories based on their file extension."""
    target_dir = Path(directory)
    if not target_dir.exists():
        print(f"Directory {directory} does not exist.")
        return

    mapping = {
        "Documents": [".pdf", ".docx", ".txt", ".md"],
        "Images": [".jpg", ".jpeg", ".png", ".svg"],
        "Code": [".c", ".cpp", ".py", ".js", ".ts", ".html", ".css"],
        "Archives": [".zip", ".tar", ".gz"]
    }

    files = [f for f in target_dir.iterdir() if f.is_file()]
    print(f"Scanned {len(files)} files in {target_dir} for categorization.")

if __name__ == "__main__":
    categorize_files(".")
