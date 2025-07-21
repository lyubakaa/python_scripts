# Import sys module to access command-line arguments via sys.argv
import sys

# Define the main function that takes the path to the log file
def count_dhcp_entries(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as f:
            count = 0  # Initialize a counter to track the number of matching lines

            # Loop through each line of the file using enumerate for line numbering (i is unused here)
            for i, line in enumerate(f):
                # Check if the line starts with 'dhcp' (case-insensitive)
                if line.lower().startswith("dhcp"):
                    count += 1  # Increment the match counter
                    # Print the matching line with its match number and strip newline
                    print(f"{count}. {line.strip()}")

            # Print the total number of matched lines after the loop
            print(f"\nTotal: {count} DHCP log entries")

    # Handle the case where the specified file does not exist
    except FileNotFoundError:
        print("The file doesn't exist or the path is incorrect.")

# Ensure the script runs only when executed directly, not when imported
if __name__ == "__main__":
    # Check that exactly one argument is passed (the log file path)
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file_path>")
        sys.exit(1)

    # Extract the log file path from the first argument
    log_file = sys.argv[1]
    # Call the function with the provided file path
    count_dhcp_entries(log_file)

