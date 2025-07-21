# file_type_summary_recursive.py
# Goal:
# Recursively walk through a directory and count how many files exist for each file extension.
# This gives an overview of the types of files across an entire directory tree.

import os  # Module for working with directories and file paths

# Step 1: Ask the user for a directory path
directory = input("Enter directory path to scan recursively: ")

# Step 2: Check if the path is a valid directory
if not os.path.isdir(directory):
    print("Error: The provided path is not a valid directory.")
    exit(1)

# Step 3: Create an empty dictionary to hold extension counts
file_types = {}  # Example: {'.txt': 10, '.log': 3}

# Step 4: Walk through the directory tree
# os.walk() returns a tuple (current_folder, subfolders, files) for each directory
for root, _, files in os.walk(directory):
    for file in files:
        # Get the extension of each file
        _, ext = os.path.splitext(file)

        # Count only files that have an extension
        if ext:
            file_types[ext] = file_types.get(ext, 0) + 1

# Step 5: Print the summary of results
print("\nRecursive File Type Summary:")
if file_types:
    for ext, count in sorted(file_types.items()):
        print(f"{ext} → {count} file(s)")
else:
    print("No files with extensions were found.")
