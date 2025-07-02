# Intermediate Exercise 2: user_directory_report.py
# Goal:
# - Practice reading and analyzing the contents of a directory
# - Count the number of files, folders, and total file size
# - Use basic file and directory handling functions in Python

import os  # Import the os module to work with file system paths and objects

# Define a function to scan and summarize a directory
def scanner(directory):
    try:
        # Get a list of items (files and folders) in the specified directory
        items = os.listdir(directory)
        
        # If the directory is empty, print a message and exit the function
        if not items:
            print("The directory is empty.")
            return

        # Initialize counters for files, folders, and total size
        file_count = 0
        folder_count = 0
        total_size = 0

        # Loop through every item in the directory
        for item_name in items:
            # Build the full path to the item
            item_path = os.path.join(directory, item_name)

            # Check if the item is a directory (folder)
            if os.path.isdir(item_path):
                folder_count += 1
                print(f"Folder:    Name: {item_name}")

            # Check if the item is a regular file
            elif os.path.isfile(item_path):
                file_count += 1
                file_size = os.path.getsize(item_path)  # Get the size in bytes
                total_size += file_size
                print(f"File:      Name: {item_name}  Size: {file_size} bytes")

            # Handle other types of items (e.g., symbolic links, sockets)
            else:
                print(f"Other:     Name: {item_name}")

        # Print a summary report after processing all items
        print("\nSummary")
        print(f"Folders:     {folder_count}")
        print(f"Files:       {file_count}")
        print(f"Total size:  {total_size} bytes")

    # Handle the case when the directory does not exist
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")

# Main program block
if __name__ == "__main__":
    # Prompt the user to input a directory path
    directory = input("Please input the full path of the directory you want to scan: ")
    
    # Call the scanner function with the user's input
    scanner(directory)
