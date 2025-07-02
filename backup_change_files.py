# Import necessary modules:
# - os: for working with file and directory paths
# - shutil: for copying files
# - sys: to access command-line arguments
import os 
import shutil
import sys

# Define the main function that will compare and back up changed files
def backup_changed_files(source_dir, backup_dir):
    # If the backup directory doesn't exist, create it
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)  # fixed typo: os.makedir -> os.makedirs
        print(f'Created a backup directory: {backup_dir}')
    else:
        print(f'Backup directory found in: {backup_dir}')

    # Initialize counters and error storage
    copied_files = 0      # Tracks how many files were copied or updated
    errors = []           # Collects errors encountered during copying

    try:
        # Loop through each item in the source directory
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)    # Full path to the source file
            backup_path = os.path.join(backup_dir, item)    # Full path to the backup file

            # Only process regular files, skip subdirectories
            if os.path.isfile(source_path):
                # Case 1: File does NOT exist in backup directory → copy it
                if not os.path.exists(backup_path):
                    shutil.copy2(source_path, backup_path)
                    copied_files += 1
                    print(f"Copied new file: {item}")

                # Case 2: File exists → compare timestamps and copy if source is newer
                else:
                    source_mtime = os.path.getmtime(source_path)
                    backup_mtime = os.path.getmtime(backup_path)

                    # If source file is newer → overwrite the backup
                    if source_mtime > backup_mtime:
                        shutil.copy2(source_path, backup_path)
                        copied_files += 1
                        print(f"Updated file: {item}")

            elif os.path.isdir(source_path):
                # For simplicity, we skip directories in this version (non-recursive)
                print(f"Skipping directory: {source_path}")
    
    # finally block runs whether or not errors occur
    finally:
        # Print a final summary of the backup operation
        print("\nBackup Summary:")
        print(f"Files copied or updated: {copied_files}")
        if errors:
            print("Errors encountered:")
            for error in errors:
                print(f"- {error}")
        else:
            print("No errors encountered.")

# Entry point of the script
if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} source_dir backup_dir")
        sys.exit(1)  # Exit the program if arguments are missing
    
    # Get the source and backup directory paths from arguments
    source_dir = sys.argv[1]
    backup_dir = sys.argv[2]

    # Call the main function to begin backup
    backup_changed_files(source_dir, backup_dir)
