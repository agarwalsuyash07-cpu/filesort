# File Sorter

A Python script that automatically organizes files in a directory by sorting them into categorized subfolders based on their file extension.

## Overview

`File_sort.py` scans a source directory (e.g., your Downloads folder), reads each file's extension, and moves it into the appropriate category subfolder inside a destination directory. Files without an extension are skipped.

## File Categories

| Folder | Extensions |
|--------|-----------|
| `imagefiles` | `.png`, `.jpg`, `.jpeg`, `.gif`, `.jfif`, `.webp`, `.html`, `.htm` |
| `pdf_files` | `.pdf`, `.PDF` |
| `DOCfiles` | `.docx`, `.xlsx` |
| `EXEfiles` | `.exe`, `.msi` |
| `ZIPfiles` | `.zip` |
| `Soundfiles` | `.mp4` |

## How It Works

1. Lists all files in the `source` directory.
2. For each file, extracts the name and extension using `os.path.splitext`.
3. Skips files with no extension (folders, extension-less files).
4. Checks which category the extension belongs to.
5. Creates the category subfolder inside `destination` if it doesn't exist.
6. Moves the file into the appropriate subfolder using `shutil.move`.

## Requirements

- Python 3.x
- Standard library only (`os`, `shutil` — no external dependencies)

## Configuration

Edit the `source` and `destination` variables at the top of `File_sort.py` to match your system paths:

```python
source = "C:/Users/YourName/Downloads"
destination = "C:/Users/YourName/Downloads/sorted"
```

## Usage

```bash
python File_sort.py
```

The script prints each filename and extension as it processes them, and logs a message for every file it moves.

## Project Structure

```
filesort/
└── File_sort.py   # Main sorting script
```

## Notes

- Files already in a category subfolder are not re-processed (the script only reads the top-level source directory).
- The commented-out block at the bottom of the script contains an unfinished MySQL integration intended to log moved files into a database table (`movedfiles`). This feature is not active.
- `.mp4` files are placed in `Soundfiles` — this folder name is a misnomer since `.mp4` is a video format; rename as needed.
