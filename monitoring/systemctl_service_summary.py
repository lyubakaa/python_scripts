### Goal: Ask the user for service names and show whether each is active or inactive using systemctl.Goal: Ask the user for service names and show whether each is active or inactive using systemctl.

import subprocess

# Get services from user input (space-separated)
services = input("Enter service names to check (e.g., ssh apache2 cron): ").split()

print("\nSystemd Service Status:\n")

# Loop through each service name
for service in services:
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )
        status = result.stdout.strip()
        print(f"{service:<15}: {status}")
    except Exception as e:
        print(f"{service:<15}: ERROR checking status → {e}")
