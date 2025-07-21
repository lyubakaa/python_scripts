import os

directory = input("Enter the directory path: ")
snapshot_file = "snapshot.txt"

# Get current file list
current_files = set(os.listdir(directory))

# Load previous snapshot (if exists)
if os.path.exists(snapshot_file):
    with open(snapshot_file, "r") as f:
        previous_files = set(line.strip() for line in f.readlines())
else:
    previous_files = set()

# Compare sets
added = current_files - previous_files
removed = previous_files - current_files

# Show changes
print("\nChanges since last snapshot:")
if added:
    print("New files:")
    for f in sorted(added):
        print("-", f)
if removed:
    print("Deleted files:")
    for f in sorted(removed):
        print("-", f)
if not added and not removed:
    print("No changes.")

# Save current snapshot
with open(snapshot_file, "w") as f:
    for filename in sorted(current_files):
        f.write(filename + "\n")
