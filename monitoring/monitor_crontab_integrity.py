import subprocess
import hashlib
import os

hash_file = "crontab_hash.txt"

# Get current crontab as string
try:
    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    crontab_content = result.stdout.strip()
except Exception as e:
    print("Failed to read crontab:", e)
    exit(1)

# Compute hash
current_hash = hashlib.sha256(crontab_content.encode()).hexdigest()

# Compare with previous hash
if os.path.exists(hash_file):
    with open(hash_file, "r") as f:
        stored_hash = f.read().strip()
    if stored_hash != current_hash:
        print("⚠️ Crontab has changed!")
    else:
        print("No changes in crontab.")
else:
    print("No previous hash found. Saving current crontab hash.")

# Save current hash
with open(hash_file, "w") as f:
    f.write(current_hash)
