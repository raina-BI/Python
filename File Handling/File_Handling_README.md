# File Organizer: Moving Files by Type

This Python script moves files from a **source directory** to a **destination directory**, specifically targeting image files. 
It organizes image files (e.g., `.jpg`, `.png`, `.gif`, etc.) into a designated folder structure, creating directories if necessary.

## Features
- Identifies and processes files with image extensions: `.gif`, `.png`, `.jpg`, `.jpeg`.
- Skips files without extensions.
- Creates destination subfolders dynamically if they do not exist.
- Moves image files from the source directory to a structured image folder.

## Prerequisites
- Python 3.x installed on your system.
- Required Python libraries:
  - **os**: For interacting with the file system.
  - **shutil**: For moving files between directories.

## Setup and Usage
### 1. Configure Source and Destination Directories
Edit the script to specify the source and destination directories:
```python
from_dir = "C:/Users/raina/Desktop/SRC_FOLDER"  # Source directory
to_dir = "C:/Users/raina/Desktop/IMG_FOLDER"    # Destination directory

