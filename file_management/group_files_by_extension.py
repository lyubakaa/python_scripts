## Goal: Scan a directory and summarize how many files exist for each file extension.

import os
from collections import defaultdict

directory = input("Enter the directory to group files by extension: ")

if not os.path.isdir(directory):
    print("Invalid directory.")
    exit(1)

# Dictionary to count extensions
extension_counts = defaultdict(int)

# Walk through the directory
for root, _, files in os.walk(directory):
    for file in files:
        ext = os.path.splitext(file)[1].lower() or "NO_EXT"
        extension_counts[ext] += 1

# Print result
print("\nFile Extension Summary:")
for ext, count in sorted(extension_counts.items()):
    print(f"{ext}: {count} file(s)")
