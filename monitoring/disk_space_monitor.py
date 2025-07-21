# disk_space_monitor.py
# Goal:
# Monitor disk space every 60 seconds on a given mount point (e.g., '/').
# If free space falls below 500 MB, print a warning and log it.
# Optional: raise an alert if the space is low for 3 consecutive checks.

import shutil                # To check disk usage
import time                  # For delays between checks
from datetime import datetime  # To log timestamps

# Step 1: Set path to monitor and threshold
path_to_monitor = "/"  # Change to '/home' or another mount point if needed
threshold_bytes = 500 * 1024 * 1024  # 500 MB in bytes

# Step 2: Define log file
log_file = "disk_alert.log"

# Step 3: Initialize failure counter
low_space_count = 0
failure_threshold = 3

# Step 4: Start monitoring loop
while True:
    try:
        # Check disk usage statistics
        usage = shutil.disk_usage(path_to_monitor)
        free = usage.free
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Print current free space
        print(f"[{timestamp}] Free space: {free // (1024 * 1024)} MB")

        if free < threshold_bytes:
            low_space_count += 1
            print(f"Warning: Free space is below 500 MB! ({free // (1024 * 1024)} MB remaining)")

            # Log the warning
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] Low disk space warning: {free // (1024 * 1024)} MB available\n")

            # Raise persistent alert if low for 3 checks in a row
            if low_space_count >= failure_threshold:
                print("ALERT: Disk space has been low for 3 consecutive checks!")
        else:
            # Reset counter if free space is sufficient again
            low_space_count = 0

    except Exception as e:
        print(f"Error checking disk space: {e}")

    # Wait 60 seconds before checking again
    time.sleep(3)
