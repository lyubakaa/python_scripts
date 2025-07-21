# monitor_nginx_status.py
# Goal:
# Periodically check a file called 'nginx.status.txt' every 30 seconds.
# If the content is not 'active', print a warning and track failures.
# If 3 failures occur in a row, raise a critical alert.

import os      # To check if the file exists
import time    # To pause between checks

# Path to the simulated status file (can be changed if needed)
status_file = "sample_nginx_status.txt"

# Initialize failure counter and threshold
failure_count = 0
failure_threshold = 3  # After 3 consecutive failures, trigger an alert

# Start the monitoring loop
while True:
    try:
        # Check if the status file exists
        if os.path.exists(status_file):
            # Open and read the content of the file
            with open(status_file, "r") as f:
                status = f.read().strip().lower()  # Normalize by stripping whitespace and converting to lowercase

            # Check the actual service status
            if status != "active": ### if status not in ("active", "started"):
                failure_count += 1  # Increment failure count
                print(f"Warning: NGINX status is '{status}'. Consecutive failures: {failure_count}")

                # If failure threshold is reached, raise an alert
                if failure_count >= failure_threshold:
                    print("ALERT: NGINX has failed 3 times in a row!")
            else:
                print("NGINX is active.")
                failure_count = 0  # Reset the failure count if status is OK
        else:
            print(f"Error: Status file '{status_file}' not found.")

    # Catch and report any unexpected runtime error
    except Exception as e:
        print(f"Unexpected error while reading status: {e}")

    # Wait 30 seconds before checking again
    time.sleep(30)
