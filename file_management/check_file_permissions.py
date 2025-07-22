# Goal:
# Check all files in a given directory (non-recursively) to:
# - Ensure their permissions match a desired value (e.g., 644)
# - Ensure their owner is the current user
# - Correct mismatches where possible
# - Print a summary of changes

import os
import stat
import pwd

# Define the desired permissions (e.g., 0o644)
desired_permission = 0o644

# Get the directory from the user
directory = input("Enter the directory to check file permissions and ownership: ")

# Validate input
if not os.path.isdir(directory):
    print("Invalid directory.")
    exit(1)

# Get current user's UID and username
current_uid = os.getuid()
current_user = pwd.getpwuid(current_uid).pw_name

print(f"\nChecking files in: {directory}")
print(f"Expected permissions: {oct(desired_permission)}")
print(f"Expected owner: {current_user} (UID: {current_uid})\n")

# Loop through files in the directory (non-recursively)
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        # Get file permission bits
        current_perm = stat.S_IMODE(os.lstat(file_path).st_mode)
        current_stat = os.stat(file_path)
        file_uid = current_stat.st_uid

        # Get owner's username (for display)
        try:
            owner = pwd.getpwuid(file_uid).pw_name
        except KeyError:
            owner = f"UID {file_uid}"

        # Show permission and owner
        print(f"{filename}: perms={oct(current_perm)}, owner={owner}")

        # Fix permissions if incorrect
        if current_perm != desired_permission:
            os.chmod(file_path, desired_permission)
            print(f" → Updated permissions to {oct(desired_permission)}")

        # Fix ownership if not owned by current user (only works on Unix)
        if file_uid != current_uid:
            try:
                os.chown(file_path, current_uid, os.getgid())
                print(f" Changed ownership to {current_user}")
            except PermissionError:
                print(" Cannot change ownership — run as root.")
            except AttributeError:
                print(" Ownership check not supported on this OS.")
