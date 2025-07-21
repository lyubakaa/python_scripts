import os
import shutil
import sys

def backup_changed_files(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Backup directory created: {backup_dir}")
    else:
        print(f"Backup directory already exists {backup_dir}")

    copied_files = 0
    errors = 0

    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            backup_path = os.path.join(backup_dir, item)

            if os.path.isfile(source_path):
                if not os.path.exists(backup_path):
                    shutil.copy2(source_path, backup_path)
                    copied_files += 1
                    print(f"Copied file: {item}")

                else:
                    source_mtime = os.path.getmtime(source_path)
                    backup_mtime = os.path.getmtime(backup_path)
                
                    if source_mtime > backup_mtime:
                        shutil.copy2(source_path, backup_path)
                        copied_files += 1
                        print(f"Updated file: {item}")
                
            elif os.path.isdir(source_path):
                print(f"Skipping directory: {source_path}")

    finally:
        print("Bakup Summary:") 
        print(f"Files copied or updated: {copied_files}")
        if errors:
            print("Errors encountered")
            for error in errors:
                print(f"- {error}")
            else:
                print("No errors encoutered")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Usage python {sys.argv[0]} <source_dir> <backup_dir>")
        sys.exit(1)

    source_dir = sys.argv[1]
    backup_dir = sys.argv[2]

    backup_changed_files(source_dir, backup_dir)