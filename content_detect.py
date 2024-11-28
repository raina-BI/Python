"""
Write a python program to automate segregating files into different folders based on the file type
"""

import os
import shutil
import time
import magic
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

# Paths
from_dir = "C:/Users/raina/Downloads"
to_dir = "C:/Users/raina/Desktop"

# Directory tree for categorizing files
dir_tree = {
    "Image_files": [".jpg", ".jpeg", ".png"],
    "Video_files": [".mp4", ".mov", ".avi"],
    "Audio_files": [".mp3", ".wav"],
    "Document_files": [".ppt", ".csv", ".pdf", ".txt"]
}

# Function to move files
def move_file(file_name, category):
    path1 = os.path.join(from_dir, file_name)
    path2 = os.path.join(to_dir, category)
    path3 = os.path.join(path2, file_name)

    if os.path.exists(path2):
        print(f"Directory exists: Moving {file_name} to {path2}")
    else:
        print(f"Creating directory: {path2}")
        os.makedirs(path2)

    shutil.move(path1, path3)
    print(f"{file_name} moved to {path3}")
    time.sleep(1)

# Class to handle file system events
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        file_name = os.path.basename(event.src_path)

        # Adding delay to ensure file is fully written
        time.sleep(2)

        # Checking for files with extensions
        for category, extensions in dir_tree.items():
            if extension in extensions:
                print(f"Downloaded: {file_name} with extension {extension}")
                move_file(file_name, category)
                return

        # Handling files without extensions
        if extension == '':
            print(f"No extension for {file_name}. Determining file type...")
            file_type = magic.from_file(event.src_path, mime=True)
            print(f"Detected file type: {file_type}")

            # Move files based on MIME type
            if file_type.startswith("image"):
                move_file(file_name, "Image_files")
            elif file_type.startswith("video"):
                move_file(file_name, "Video_files")
            elif file_type.startswith("audio"):
                move_file(file_name, "Audio_files")
            elif file_type.startswith("text") or "pdf" in file_type:
                move_file(file_name, "Document_files")
            else:
                print(f"Unknown file type for {file_name}. Leaving in the download folder.")

# Initialize event handler and observer
event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(30)  # Keep the observer running
        print("Monitoring...")
except KeyboardInterrupt:
    print("Stopped by user.")
    observer.stop()

observer.join()
