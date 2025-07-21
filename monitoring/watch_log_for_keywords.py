# watch_log_for_keywords.py
# Goal:
# Monitor a log file (e.g., /var/log/auth.log) every 60 seconds.
# If 5 or more "Failed password" entries are found in a scan, alert the user.
# Optionally, log these alerts to a file.

import time                         # Used to wait between checks
from datetime import datetime       # For timestamps in alerts

# Ask the user for the log file path
log_file = input("Enter the path to the log file (e.g., /var/log/auth.log): ")

# Define the alert log file to store triggered warnings
alert_log = "sample_output_alert.log"

# Start an infinite monitoring loop
while True:
    try:
        # Step 1: Read the log file
        with open(log_file, "r") as f:
            lines = f.readlines()

        # Step 2: Filter for lines containing the keyword (case-insensitive)
        keyword = "failed password"
        failed_lines = [line for line in lines if keyword in line.lower()]

        # Step 3: Count how many lines matched
        match_count = len(failed_lines)

        # Step 4: Alert if threshold is exceeded
        if match_count >= 5:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Warning: Possible brute-force login attempt detected at {timestamp}!")
            print(f"Matches in last scan: {match_count}")

            # Step 5: Save the alert to the alert log
            with open(alert_log, "a") as alert:
                alert.write(f"[{timestamp}] Detected {match_count} failed login attempts\n")

        else:
            print(f"Scan complete. Found {match_count} failed login attempts.")

    except FileNotFoundError:
        print(f"Error: Could not find log file at {log_file}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Step 6: Wait 60 seconds before scanning again
    time.sleep(5)
