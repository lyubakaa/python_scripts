# Exercise: Generate a CSV report of file sizes in a directory (non-recursive).
# The CSV should list each file's name and size in bytes, with headers.
import os
import csv

directory = input("Enter directory: ")
if not os.path.isdir(directory):
    print("Invalid directory")
    exit(1)

csv_path = os.path.join(directory, "file_sizes.csv")
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "size_bytes"])
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            writer.writerow([filename, size])
print(f"CSV report written to {csv_path}") 