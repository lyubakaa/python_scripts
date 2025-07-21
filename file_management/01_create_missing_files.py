# ✅ Beginner Exercise
# Create a script that:
# 1. Checks if the following files exist in the current directory:
#    - exam_file1.txt
#    - exam_file2.txt
#    - exam_file3.txt
# 2. If any of them don't exist, create them.
# 3. Ensure they all have permission 644.
# 4. Set their ownership to the current user (if supported by OS).

# Your code here:
import os

# Get file names from user input
input_str = input("Names of the files to check for (comma-separated): ")

files = [name.strip() for name in input_str.split(',') if name.strip()]

for name in files:
    if not os.path.exists(name):
        with open(name, 'w') as f:
            f.write("")  # create empty file
        os.chmod(name, 0o644)
        try:
            os.chown(name, os.getuid(), os.getgid())  # Fix: os.chown not os.chwon
        except AttributeError:
            # os.chown might not be available on Windows
            pass
        print(f"Created file: {name}")
    else:
        print(f"{name} already exists.")
