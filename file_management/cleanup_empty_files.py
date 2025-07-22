# ✅ Goal:
# Scan a directory recursively and delete all empty files.
# - A file is considered empty if its size is 0 bytes.
# - Log each deletion to the console.
# - Print a summary at the end showing how many files were removed.

import os

# Ask user for the directory to clean
directory = input("Enter the directory to clean up empty files: ")

# Validate input
if not os.path.isdir(directory):
    print("Invalid directory.")
    exit(1)

deleted_count = 0

# Recursively scan files
for root, _, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(root, filename)

        # Check if the file is empty
        if os.path.isfile(filepath) and os.path.getsize(filepath) == 0:
            try:
                os.remove(filepath)
                deleted_count += 1
                print(f"Deleted empty file: {filepath}")
            except Exception as e:
                print(f"Failed to delete {filepath}: {e}")

# Summary
print(f"\nCleanup complete. Total empty files deleted: {deleted_count}")
