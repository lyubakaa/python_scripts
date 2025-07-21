# ✅ Beginner Exercise
# Write a Python script that lists all files in the current directory
# and prints their sizes in bytes.

# Example output:
# file1.txt - 204 bytes
# file2.log - 1000 bytes

# Your code here:
import os 

directory = input(f"Input the full path of the directory: ")

for file in os.listdir(directory):
    if os.path.isfile(file):
        size = os.path.getsize(file)
        print(f"{file}: {size} bytes ")