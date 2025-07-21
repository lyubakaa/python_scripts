import os 

directory = input(f"Enter the full path of the directory: ")

if not os.path.isdir(directory):
    print("Invalid directory")
    exit(1)

empty_files = []

for file in os.listdir(directory):
    full_path = os.path.join(directory, file)
    if os.path.isfile(full_path) and os.path.getsize(full_path) == 0:
        empty_files.append(full_path)

if empty_files: 
    print(f"Found {len(empty_files)} empty files: ")
    for f in empty_files:
        print("-", f)

    delete = input("\nDo you want to delete them? (y/n): ").strip().lower()
    if delete == 'y':
        for f in empty_files:
            os.remove(f)
        print("Empty files deleted")
    else:
        print("No files were deleted")

else:
    print("No empty files found.")