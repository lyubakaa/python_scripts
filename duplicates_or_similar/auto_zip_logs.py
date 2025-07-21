# Import required modules:
# - os: for file path and directory handling
# - sys: for accepting command-line arguments
# - zipfile: to create and manage zip archives
import os 
import sys 
import zipfile

# Define the main function that compresses .log files into a zip archive
def zip_logs(directory, zip_name):
    # Check if the provided directory exists
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return  # Exit the function early if the directory is invalid

    # Construct the full path to the output zip file inside the given directory
    zip_path = os.path.join(directory, zip_name)
    file_count = 0  # Track how many files were added to the archive

    try:
        # Open a new zip file in write mode ('w' will overwrite if it exists)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            # Loop through all items in the specified directory
            for item in os.listdir(directory):
                # Only process files that end with .log
                if item.endswith('.log'):
                    file_path = os.path.join(directory, item)

                    # Make sure the path points to a file, not a folder
                    if os.path.isfile(file_path):
                        # Add the file to the zip, using just the filename (not full path)
                        zipf.write(file_path, arcname=item)
                        file_count += 1
                        print(f"Added: {item}")

        # After all matching files are added, print summary information
        print(f"\nTotal .log files added: {file_count}")
        print(f"Output zip file created at: {zip_path}")

    except Exception as e:
        # Handle any unexpected errors during the zipping process
        print(f"Error occurred while creating zip file: {e}")

# Ensure this script runs only when executed directly, not when imported
if __name__ == "__main__":
    # Check if exactly 2 arguments are provided (directory path and zip filename)
    if len(sys.argv) != 3:
        print(f"USAGE: python {sys.argv[0]} <directory_path> <zip_name>")
        sys.exit(1)

    # Get the arguments from the command line
    directory = sys.argv[1]  # The folder to scan for .log files
    zip_name = sys.argv[2]   # The desired name for the zip archive

    # Call the main function with user-supplied arguments
    zip_logs(directory, zip_name)
