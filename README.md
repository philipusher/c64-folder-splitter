# C64 Mini / Maxi Folder Splitter

The C64 Mini and C64 Maxi have a limitation: each folder can only contain **256 files**.  
If you dump a large game collection into a single folder, many titles won’t show up.

This Python script solves that problem by automatically reorganising your collection:
- Recursively scans all subfolders (e.g. D:\c64).
- Groups files alphabetically by their first letter.
- If a letter group has more than 256 files, it creates numbered subfolders (A1, A2, …).
- Ensures no folder ever exceeds the 256‑file limit.

## Usage

1. Install Python 3 from https://www.python.org/downloads/
2. Download `c64_split_folders.py` from this repo.
3. Edit the `root` variable in the script to point to your C64 collection folder, e.g.:

   root = r"D:\c64"

4. Run the script from a terminal or command prompt:

   python split_folders.py

5. Copy the reorganised folder structure onto your USB stick and plug it into your C64 Mini/Maxi.

## Notes
- Non‑alphabetic filenames (e.g. starting with numbers or symbols) are placed into #1, #2, etc.
- The script **moves files**, so test on a copy of your collection first.

- Works on Windows, macOS, and Linux.
