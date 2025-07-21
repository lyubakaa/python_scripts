import os

def scanner(directory):

    try:
        items = os.listdir(directory)

        if not items:
            print("The directory is empty")
            return
    
        file_count = 0
        folder_count = 0
        total_size = 0

        for item_name in items:
            item_path = os.path.join(directory, item_name)
            
            if os.path.isdir(directory):
                folder_count += 1
                print(f"Folder:    Name: {item_name}")
            elif os.path.isfile(directory):
                file_count += 1
                file_size = os.path.getsize(item_path)
                total_size += file_size
                print(f"File:      Name: {item_name}  Size: {file_size} bytes")

            else:
                print(f"Other:     Name:  ")

        print("\nSummary")
        print(f"Folders:     {folder_count}")
        print(f"Files:       {file_count}")
        print(f"Total size:  {total_size} bytes")

    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist")

if __name__ == "__main__":

    directory = input("Please input")