# Exercise: Monitor a log file in real-time for a user-supplied regex pattern.
# Print matching lines and alert every time 10 matches are found, then reset the counter.
import re
import time

def tail_f(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

if __name__ == "__main__":
    log_path = input("Enter path to log file: ")
    pattern = input("Enter regex pattern to monitor: ")
    try:
        regex = re.compile(pattern)
    except re.error as e:
        print(f"Invalid regex: {e}")
        exit(1)
    try:
        with open(log_path, 'r') as f:
            match_count = 0
            for line in tail_f(f):
                if regex.search(line):
                    print(f"MATCH: {line.strip()}")
                    match_count += 1
                    if match_count == 10:
                        print("ALERT: 10 matches found! Counter reset.")
                        match_count = 0
    except FileNotFoundError:
        print("Log file not found.") 