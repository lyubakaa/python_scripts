## Goal: Recursively search all .log files in a directory for a keyword and print matching lines with the file path.

import os

# Get the base directory and keyword from user
directory = input("Enter the directory to search recursively: ")
keyword = input("Enter the keyword to search for: ").lower()

if not os.path.isdir(directory):
    print("Invalid directory.")
    exit(1)

print(f"\nSearching for '{keyword}' in all .log files under: {directory}\n")

# Walk through all subdirectories and files
for root, _, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".log"):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", errors="ignore") as f:
                    for line_number, line in enumerate(f, 1):
                        if keyword in line.lower():
                            print(f"{filepath} (line {line_number}): {line.strip()}")
            except Exception as e:
                print(f"Could not read {filepath}: {e}")
