# Exercise: Compare files with the same name in two directories.
# Print the names of files that differ in content. Useful for practicing file comparison.
import os

def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        return f1.read() == f2.read()

if __name__ == "__main__":
    dir1 = input("Enter first directory: ")
    dir2 = input("Enter second directory: ")
    if not (os.path.isdir(dir1) and os.path.isdir(dir2)):
        print("One or both directories are invalid.")
        exit(1)
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    common = files1 & files2
    for fname in sorted(common):
        path1 = os.path.join(dir1, fname)
        path2 = os.path.join(dir2, fname)
        if os.path.isfile(path1) and os.path.isfile(path2):
            if not compare_files(path1, path2):
                print(f"Files differ: {fname}") 