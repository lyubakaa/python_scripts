# check_duplicate_filenames.py
# Goal:
# Compare two user-specified directories and print any filenames that appear in both directories.
# This helps detect name collisions or redundancies.

import os  # Module for filesystem interaction

# Step 1: Ask the user for two directory paths
dir1 = input("Enter the first directory path: ")
dir2 = input("Enter the second directory path: ")

# Step 2: Validate both inputs to ensure they are directories
if not os.path.isdir(dir1) or not os.path.isdir(dir2):
    print("Error: One or both of the provided paths are not valid directories.")
    exit(1)

# Step 3: List all items in both directories and convert them to sets
# We only compare filenames, not full paths or file content
files1 = set(os.listdir(dir1))
files2 = set(os.listdir(dir2))

# Step 4: Find common filenames using set intersection
duplicates = files1.intersection(files2)

# Step 5: Print the results
if duplicates:
    print("\nDuplicate filenames found in both directories:")
    for filename in sorted(duplicates):
        print(f"- {filename}")
else:
    print("\nNo duplicate filenames found.")
