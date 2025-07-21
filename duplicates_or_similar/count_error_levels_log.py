# ✅ Goal Recap
# Given a log file, count how many times the words:

# INFO

# WARNING

# ERROR
# appear (case-insensitive is recommended), and print a summary like:

# Ask the user for the path to the log file
log_file = input("Enter the path to the log file: ")

# Initialize counters
counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

try:
    with open(log_file, "r") as f:
        for line in f:
            upper_line = line.upper()  # make it case-insensitive
            for level in counts:
                if level in upper_line:
                    counts[level] += 1

    # Print summary
    print("\nSummary:")
    for level in ["INFO", "WARNING", "ERROR"]:
        print(f"{level}: {counts[level]}")

except FileNotFoundError:
    print("Log file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
