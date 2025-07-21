# check_ssh_service_live.py
# Goal:
# Every 60 seconds, check if the SSH service is active using `systemctl`.
# Log the result with a timestamp to a file, and print a warning if SSH is down.

import subprocess        # To run system commands like `systemctl`
import time              # For waiting between checks
from datetime import datetime  # To generate readable timestamps

# Define the output log file
log_file = input("Enter the path: ")

# Start the continuous monitoring loop
while True:
    # Step 1: Get the current time as a readable string
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Step 2: Run 'systemctl is-active ssh' and capture its output
        result = subprocess.run(
            ["systemctl", "is-active", "ssh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Extract the actual status (like 'active', 'inactive', 'failed', etc.)
        status = result.stdout.strip()

        # Step 3: Prepare the log entry
        log_entry = f"[{timestamp}] SSH status: {status}\n"

        # Step 4: Append the result to the log file
        with open(log_file, "a") as f:
            f.write(log_entry)

        # Step 5: Print a warning if SSH is not active
        if status != "active":
            print(f"WARNING: SSH service is down! Status = '{status}'")

        else:
            print(f"{timestamp} - SSH is active.")

    except Exception as e:
        print(f"Error while checking SSH service: {e}")

    # Step 6: Wait 60 seconds before checking again
    time.sleep(60)
