# ✅ Intermediate Exercise
# Given a log file (e.g. sample_dhcp.log), count how many lines
# start with 'DHCP' (case-insensitive) and print them numbered.
#
# Example:
# 1. DHCP... 192.168.1.12
# 2. DHCP13.. 192.168.1.15
# Total: 2 DHCP log entries

# Your code here:
log_file = input(f"Full path to the log file: ")

try:
    with open(log_file, "r") as f:
        count = 0
        for i, line in enumerate(f, 1):
            if line.lower().startswith("dhcp"):
                count += 1
                print(f"{count}. {line.strip()}")
        print(f"Total: {count} DHCP log entries")
except FileNotFoundError:
    print(f"Log file not found: {log_file}")