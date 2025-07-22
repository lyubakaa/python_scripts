# Check if specific files in a directory have the correct permissions (e.g. 644 or 755). Fix them if they don’t match.

import os
import stat

# Define desired permissions in octal (e.g., 0o644)
desired_permission = 0o644

# Get directory from user
directory = input("Enter the directory to check file permissions: ")

# Validate directory
if not os.path.isdir(directory):
    print("Invalid directory.")
    exit(1)

print(f"Checking permissions in: {directory}")

# Loop through files only (non-recursive)
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        # Get current permission bits
        current_perm = stat.S_IMODE(os.lstat(file_path).st_mode)
        
        # Print current permission
        print(f"{filename}: current permission = {oct(current_perm)}")

        # If different from desired, fix it
        if current_perm != desired_permission:
            os.chmod(file_path, desired_permission)
            print(f"→ Updated to {oct(desired_permission)}")
