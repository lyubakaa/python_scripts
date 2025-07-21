import os

directory = input("Enter the directory: ")

if not os.path.isdir(directory):
    print("Invalid directory")
    exit(1)


try: 
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            old_path = os.path.join(directory, filename)
            new_filename = filename.rsplit(".", 1)[0] + ".log"
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

except Exception as e:
    print(f"Error {e}")            