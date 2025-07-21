# auto_restart_apache.py
# Goal:
# Monitor the Apache2 service every 60 seconds.
# If it's not running (status != 'active'), restart it automatically
# and log the action with a timestamp to 'apache_restart.log'.

import subprocess              # For running system commands
import time                    # To pause between checks
from datetime import datetime  # For timestamping log entries

# Log file to record restart events
log_file = "apache_restart.log"

# Start infinite monitoring loop
while True:
    try:
        # Step 1: Check Apache service status
        result = subprocess.run(
            ["systemctl", "is-active", "apache2"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        status = result.stdout.strip()

        # Step 2: If Apache is NOT running, attempt restart
        if status != "active":
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Apache status = '{status}' → restarting service...")

            # Attempt to restart Apache (requires sudo permissions)
            restart = subprocess.run(
                ["sudo", "systemctl", "restart", "apache2"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Step 3: Log the restart event
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] Apache was '{status}' → restart attempted.\n")

        else:
            print(f"Apache is running normally.")

    except Exception as e:
        print(f"Error while checking/restarting Apache: {e}")

    # Wait 60 seconds before the next check
    time.sleep(60)
