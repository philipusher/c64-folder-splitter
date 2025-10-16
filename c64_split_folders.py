import os
import shutil
from collections import defaultdict

MAX_FILES = 256

def split_by_letter(folder_path):
    """Split files into alphabetic subfolders, numbering them if > MAX_FILES."""
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if len(files) <= MAX_FILES:
        return  # Nothing to do
    
    print(f"Splitting folder: {folder_path} ({len(files)} files)")
    
    # Group files by their starting letter (case-insensitive)
    groups = defaultdict(list)
    for f in sorted(files, key=str.lower):
        first_letter = f[0].upper()
        if not first_letter.isalpha():
            first_letter = "#"  # Non-alphabetic bucket
        groups[first_letter].append(f)
    
    # For each letter group, create subfolders with numbering if needed
    for letter, group_files in groups.items():
        for i in range(0, len(group_files), MAX_FILES):
            chunk = group_files[i:i+MAX_FILES]
            subfolder_name = f"{letter}{i // MAX_FILES + 1}"
            subfolder_path = os.path.join(folder_path, subfolder_name)
            os.makedirs(subfolder_path, exist_ok=True)
            
            for file in chunk:
                src = os.path.join(folder_path, file)
                dst = os.path.join(subfolder_path, file)
                shutil.move(src, dst)


def explore_and_split(root_folder):
    """Recursively explore folders and split them if needed."""
    for dirpath, dirnames, filenames in os.walk(root_folder):
        split_by_letter(dirpath)


if __name__ == "__main__":
    root = r"D:\c64"   # Your folder path
    explore_and_split(root)
    print("Done.")