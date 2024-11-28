"""
Python program to move files from one directory to other
@author: raina
"""

import os
import shutil

from_dir = "C:/Users/raina/Desktop/SRC_FOLDER"  # Source directory
to_dir = "C:/Users/raina/Desktop/IMG_FOLDER"    # Destination directory

# List all files in the source directory
list_of_files = os.listdir(from_dir)
print("Files in source directory:", list_of_files)

# Iterate through the files in the source directory
for file_name in list_of_files:
    # Split the file name and its extension
    name, extension = os.path.splitext(file_name)
    
    # Skip files with no extension
    if extension == "":
        continue
    
    # Process only image files
    if extension in ['.gif', '.png', '.jpg', '.jpeg']:
        # Build paths using os.path.join for better compatibility
        path1 = os.path.join(from_dir, file_name)  # Full path to the source file
        path2 = os.path.join(to_dir, "imagefiles") # Directory to store images
        path3 = os.path.join(path2, file_name)     # Destination path for the file
        
        # Check if the destination directory exists
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path3}...")
            shutil.move(path1, path3)
        else:
            # Create the directory if it doesn't exist
            os.mkdir(path2)
            print(f"Created directory {path2}. Moving {file_name}...")
            shutil.move(path1, path3)

print("File transfer completed.")
