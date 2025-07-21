# list_recent_files.py
# Goal:
# Scan a directory and list all files modified within the last N days (non-recursively),
# sorted from most recent to oldest.

import os         # For file and directory handling
import time       # For working with timestamps
import datetime   # For human-readable date formatting

# Step 1: Ask the user to provide a directory path
directory = input("Enter directory path to scan: ")

# Step 2: Validate the directory
if not os.path.isdir(directory):
    print("Error: The provided path is not a valid directory.")
    exit(1)

# Step 3: Ask how many days back to look
try:
    days = int(input("Enter the number of days to look back: "))
except ValueError:
    print("Error: Please enter a valid number of days.")
    exit(1)

# Step 4: Calculate the cutoff timestamp
now = time.time()                    # Current time in seconds since epoch
cutoff = now - (days * 86400)        # Time N days ago (86400 seconds per day)

# Step 5: Loop through files and select recently modified ones
recent_files = []

for item in os.listdir(directory):
    full_path = os.path.join(directory, item)

    if os.path.isfile(full_path):
        modified_time = os.path.getmtime(full_path)  # Get last modification time

        if modified_time >= cutoff:
            recent_files.append((item, modified_time))  # Store file name and mtime

# Step 6: Sort files by modification time (newest first)
recent_files.sort(key=lambda x: x[1], reverse=True)

# Step 7: Display the results
print(f"\nFiles modified in the last {days} day(s):\n")

if recent_files:
    for filename, mtime in recent_files:
        readable_time = datetime.datetime.fromtimestamp(mtime)  # Convert to readable format
        print(f"{filename} - Last modified: {readable_time}")
else:
    print("No files modified in the given time range.")
