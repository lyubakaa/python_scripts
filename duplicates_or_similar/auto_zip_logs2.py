import os
import sys
import zipfile

def zip_logs(directory, zip_name):
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return
    
    zip_path = os.path.join(directory, zip_name)
    file_count = 0 

    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for item in os.listdir(directory):
                if item.endswith('.log'):
                    file_path = os.path.join(directory, item)
                
                    if os.path.isfile(file_path):
                        zipf.write(file_path, arcname=item)
                        file_count += 1
                        print(f"Added {item}")
        
        print(f"\nTotal .log files added: {file_count}")
        print(f"Output zip file created at: {zip_path}")
    
    except Exception as e:
        print(f"Error occured when handling zip file: {e}")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <directory_path> <zip_path>")
        sys.exit(1)

        directory = sys.argv[1]
        zip_name = sys.argv[2]

        zip_logs(directory, zip_name)