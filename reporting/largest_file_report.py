# largest_files_report.py
# Goal:
# Scan a user-specified directory and identify the top 3 largest files.
# Also calculate the total size of all files (non-recursively).

import os  # Required for working with directories and files

# Step 1: Ask the user for the directory path
directory = input("Enter the directory path: ")

# Step 2: Validate that the input is a real directory
if not os.path.isdir(directory):
    print("Error: The provided path is not a valid directory.")
    exit(1)

# Step 3: Initialize a list to hold file name and size pairs
file_list = []

# Step 4: Loop through each item in the directory
for item in os.listdir(directory):
    full_path = os.path.join(directory, item)  # Build full file path

    # Step 5: Check if the item is a regular file
    if os.path.isfile(full_path):
        size = os.path.getsize(full_path)  # Get file size in bytes
        file_list.append((item, size))     # Save tuple: (filename, size)

# Step 6: Sort the file list by size in descending order
file_list.sort(key=lambda x: x[1], reverse=True)

# Step 7: Print the top 3 largest files
print("\nTop 3 largest files:")
for i, (filename, size) in enumerate(file_list[:3], start=1):
    print(f"{i}. {filename} - {size} bytes")

# Step 8: Calculate and print the total size of all files
total_size = sum(size for _, size in file_list)
print(f"\nTotal size of all files: {total_size} bytes")
