import os
import shutil

from_dir = "C:/Users/raina/Desktop/SRC_FOLDER"  # Source directory
to_dir = "C:/Users/raina/Desktop"    # Destination directory

# List all files in the source directory
try:
    list_of_files = os.listdir(from_dir)
    print("Files in source directory:", list_of_files)
except Exception as e:
    print(f"Error accessing source directory: {e}")
    exit()

# Check if the destination directory exists
if not os.path.exists(to_dir):
    print(f"Destination directory {to_dir} does not exist.")
    exit()

# Iterate through the files in the source directory
for file_name in list_of_files:
    # Split the file name and its extension
    name, extension = os.path.splitext(file_name)
    
    # Skip files with no extension
    if extension == "":
        print(f"Skipping {file_name}, no extension found.")
        continue
    
    # Process only image files
    if extension.lower() in ['.gif', '.png', '.jpg', '.jpeg']:
        # Build paths using os.path.join for better compatibility
        path1 = os.path.join(from_dir, file_name)  # Full path to the source file
        path2 = os.path.join(to_dir, "IMG_FOLDER") # Directory to store images
        path3 = os.path.join(path2, file_name)     # Destination path for the file
        
        print(f"Processing {file_name}: {path1} -> {path3}")
        
        # Check if the destination directory exists
        if not os.path.exists(path2):
            try:
                os.mkdir(path2)
                print(f"Created directory {path2}")
            except Exception as e:
                print(f"Error creating directory {path2}: {e}")
                continue
        
        # Move the file
        try:
            shutil.move(path1, path3)
            print(f"Moved {file_name} to {path3}")
        except Exception as e:
            print(f"Error moving {file_name}: {e}")
    else:
        print(f"Skipping {file_name}, not an image file.")

print("File transfer completed.")
