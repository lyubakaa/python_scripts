# Monitor a systemd service (e.g. apache2 or ssh) using:
#     systemctl is-active <service>
# If it's not active:
# - Restart it using 'sudo systemctl restart <service>'
# - Log the restart to a file with a timestamp

import subprocess
import time
from datetime import datetime

# Name of the service to monitor (change to 'ssh', 'nginx', etc. if needed)
service_name = "apache2"
log_file = "service_monitor.log"

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(log_file, "a") as f:
        f.write(entry + "\n")

def is_service_active(service):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True, text=True
        )
        return result.stdout.strip() == "active"
    except Exception as e:
        log_event(f"Error checking service status: {e}")
        return False

def restart_service(service):
    try:
        subprocess.run(["sudo", "systemctl", "restart", service], check=True)
        log_event(f"Service '{service}' was restarted successfully.")
    except subprocess.CalledProcessError as e:
        log_event(f"⚠️ Failed to restart service '{service}': {e}")

# Monitor loop
print(f"Monitoring systemd service: {service_name} (press Ctrl+C to stop)\n")

try:
    while True:
        if not is_service_active(service_name):
            log_event(f"Service '{service_name}' is NOT active. Attempting restart...")
            restart_service(service_name)
        else:
            print(f"{service_name} is active.")

        time.sleep(60)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
