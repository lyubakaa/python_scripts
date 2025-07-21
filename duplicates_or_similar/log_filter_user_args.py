# ✅ Intermediate Exercise 3: log_filter.py
# 🔹 Goal: Practice reading and analyzing log files with command-line arguments

# Import required modules:
# - os (optional here, useful for future file checks)
# - sys to access command-line arguments passed by the user
import os
import sys

# Define a function to filter log entries by a keyword
def filter_log(filepath, keyword):
    match_count = 0  # Initialize a counter for matched lines

    try:
        # Try to open the log file in read mode
        with open(filepath, 'r') as f:
            # Loop through each line in the file
            for line in f:
                # Perform a case-insensitive keyword search using .lower()
                if keyword.lower() in line.lower():
                    match_count += 1                    # Increment the match counter
                    print(line.strip())                 # Print the matching line without newline

        # After all lines have been checked, print total matches
        print(f"\nTotal matches found: {match_count}")

    # Handle the case where the file path is invalid or file does not exist
    except FileNotFoundError:
        print(f"File not found: {filepath}")

# Main program block — only runs if script is executed directly
if __name__ == "__main__":
    # Check if the required arguments are passed (script, filepath, keyword)
    if len(sys.argv) < 3:
        print("Usage: python log_filter.py <file_path> <keyword>")
        sys.exit(1)  # Exit the program with error code

    # Extract command-line arguments into variables
    filepath = sys.argv[1]  # Path to the log file
    keyword = sys.argv[2]   # Keyword to search for in the log

    # Call the filter function with the provided arguments
    filter_log(filepath, keyword)
