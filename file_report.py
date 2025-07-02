# ✅ Beginner Exercise 1: simple_file_report.py
# 🔹 Goal: Learn to read a file and count lines, words, and characters

# Import the os module — useful when working with files and file paths
import os

# Define a function named `counter` that takes a filename as input
def counter(fname):
    try:
        # Attempt to open the file in read mode
        with open(fname, 'r') as f:
            # Initialize counters for lines, words, and characters
            line_count = 0
            word_count = 0
            char_count = 0

            # Loop through each line in the file
            for line in f:
                line_count += 1                # Increment line count
                char_count += len(line)        # Add the number of characters in the line
                words = line.split()           # Split the line into words
                word_count += len(words)       # Count words in the line and add to total
            
            # After processing the file, print a summary of the counts
            print("📊 File analysis summary:\n")
            print(f"🧮 Character count: {char_count}")
            print(f"📝 Word count: {word_count}")
            print(f"📏 Line count: {line_count}")

    # Handle the case where the file does not exist or can't be opened
    except FileNotFoundError:
        print("❌ Error: File not found or cannot be opened.")

# Ask the user to input the file name they want to analyze
fname = input("📂 Enter the name of the file: ")

# Call the counter function with the filename provided by the user
counter(fname)
