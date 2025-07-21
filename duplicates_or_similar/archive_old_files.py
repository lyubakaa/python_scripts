import os
import time
from zipfile import ZipFile

path = input("Directory to scan: ")
days = int(input("Archive files older than how many days? "))
archive_dir = os.path.join(path, "archive")
os.makedirs(archive_dir, exist_ok=True)

threshold_time = time.time() - (days * 86400)
archived_files = []

# Walk through directory
for root, _, files in os.walk(path):
    if archive_dir in root:
        continue  # skip already archived files
    for file in files:
        full_path = os.path.join(root, file)
        if os.path.isfile(full_path) and os.path.getmtime(full_path) < threshold_time:
            archived_files.append(full_path)

# Move and zip
for f in archived_files:
    base_name = os.path.basename(f)
    zip_name = base_name + ".zip"
    zip_path = os.path.join(archive_dir, zip_name)
    with ZipFile(zip_path, "w") as zipf:
        zipf.write(f, arcname=base_name)
    os.remove(f)
    print(f"Archived: {f} → {zip_path}")
