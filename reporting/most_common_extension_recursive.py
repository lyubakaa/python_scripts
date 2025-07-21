# Exercise: Recursively scan a directory and print the most common file extension and its count.
# This helps practice directory traversal and file extension counting in Python.
import os
from collections import Counter

def get_all_extensions(directory):
    extensions = []
    for root, _, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext:
                extensions.append(ext.lower())
    return extensions

if __name__ == "__main__":
    directory = input("Enter directory to scan recursively: ")
    if not os.path.isdir(directory):
        print("Invalid directory")
        exit(1)
    extensions = get_all_extensions(directory)
    if not extensions:
        print("No files with extensions found.")
    else:
        counter = Counter(extensions)
        most_common, count = counter.most_common(1)[0]
        print(f"Most common extension: {most_common} ({count} files)") 