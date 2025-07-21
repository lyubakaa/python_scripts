# ✅ Intermediate Exercise
# Scan a given log file for lines containing 'Failed password'
# (case-insensitive). Count them and print the result.

# Your code here:

log_file = "sample.log"

try:
    with open(log_file, "r") as f:
        count = sum(1 for line in f if "failed password" in line.lower())
        print(f"Failed login attempts: {count}")
        
except FileNotFoundError:
    print("Log file not found.")