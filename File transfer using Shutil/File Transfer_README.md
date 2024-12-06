# File Organizer: Moving Image Files with Error Handling

This Python script organizes and moves **image files** (e.g., `.jpg`, `.png`, `.gif`, `.jpeg`) from a specified source directory to a destination directory. 
It includes error handling to address missing directories, inaccessible files, and unsupported file types.

## Features
- **File Type Detection**: Processes only image files based on their extensions.
- **Directory Creation**: Dynamically creates a subdirectory (`IMG_FOLDER`) in the destination if it doesn't already exist.
- **Error Handling**:
  - Checks for the existence of source and destination directories.
  - Skips files without extensions or unsupported file types.
  - Gracefully handles exceptions during directory creation and file movement.

## Prerequisites
- Python 3.x
- No additional libraries are required as it uses built-in modules (`os`, `shutil`).

## Setup and Usage
### 1. Configure Directories
Edit the script to specify:
- **Source Directory**: Folder containing the files to be moved.
  ```python
  from_dir = "C:/Users/raina/Desktop/SRC_FOLDER"
