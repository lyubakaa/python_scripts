import os

directory = input("Enter the directory path: ")

if not os.path.isdir(directory):
    print("Error")
    exit(1)


file_types = {}

for item in os.listdir(directory):
    full_path = os.path.join(directory, item)

    if os.path.isfile(full_path):

        _, ext = os.path.splitext(item)

        if ext:

            file_types[ext] = file_types.get(ext, 0) + 1

print("\nFile Type Summaary")
if file_types:
    for ext,count in file_types.items():
        print(f"{ext}, -> {count} files(s)")
    
else:
    print("No files with extentions found.")