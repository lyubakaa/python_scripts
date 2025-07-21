# Exercise: Batch rename all files in a directory by adding a user-supplied prefix to each filename.
# This helps practice file renaming and string manipulation in Python.
import os

directory = input("Enter directory: ")
prefix = input("Enter prefix to add: ")

if not os.path.isdir(directory):
    print("Invalid directory")
    exit(1)

for filename in os.listdir(directory):
    old_path = os.path.join(directory, filename)
    if os.path.isfile(old_path):
        new_filename = prefix + filename
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}") 