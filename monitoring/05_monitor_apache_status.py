# Every 60 seconds:
# - Open a file called 'apache.status.txt'
# - If it doesn't contain the word 'active', print a warning and log the failure.
# - If failures happen 3 times in a row, raise an alert.

import time
from datetime import datetime
import os

status_file = "apache.status.txt"
log_file = "apache_monitor.log"

failure_count = 0  # Track consecutive failures

def log_warning(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(log_file, "a") as f:
        f.write(entry + "\n")

print("Starting Apache status monitor. Press Ctrl+C to stop.")

while True:
    try:
        if not os.path.exists(status_file):
            log_warning(f"Status file '{status_file}' not found.")
            failure_count += 1
        else:
            with open(status_file, "r") as f:
                content = f.read().strip().lower()

            if "active" not in content:
                failure_count += 1
                log_warning(f"Apache status is not active. Consecutive failures: {failure_count}")
            else:
                print("Apache is active.")
                failure_count = 0  # Reset on success

        if failure_count >= 3:
            log_warning("⚠️ ALERT: Apache has failed 3 times in a row!")
            failure_count = 0  # Reset to avoid repeated alerts

    except Exception as e:
        log_warning(f"Unexpected error: {e}")

    time.sleep(60)

