"""
Write a python program to track the changes in the system when you download any file.
"""

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

# Set up logging to track the changes and log them to a file
logging.basicConfig(filename="file_changes.log", 
                    level=logging.INFO, 
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

# Path to the directory you want to monitor (Downloads folder)
downloads_folder = "C:/Users/raina/Downloads"

# Event Handler class to handle events (file created, modified, deleted)
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        file_name = os.path.basename(event.src_path)
        logging.info(f"File created: {file_name} at {event.src_path}")
        print(f"File created: {file_name}")

    def on_modified(self, event):
        file_name = os.path.basename(event.src_path)
        logging.info(f"File modified: {file_name} at {event.src_path}")
        print(f"File modified: {file_name}")

    def on_moved(self, event):
        file_name = os.path.basename(event.src_path)
        dest_name = os.path.basename(event.dest_path)
        logging.info(f"File moved: {file_name} from {event.src_path} to {event.dest_path}")
        print(f"File moved: {file_name} from {event.src_path} to {event.dest_path}")

    def on_deleted(self, event):
        file_name = os.path.basename(event.src_path)
        logging.info(f"File deleted: {file_name} at {event.src_path}")
        print(f"File deleted: {file_name}")

# Set up Observer to monitor the directory
observer = Observer()
event_handler = FileEventHandler()
observer.schedule(event_handler, path=downloads_folder, recursive=False)

# Start the observer
observer.start()
print(f"Monitoring changes in folder: {downloads_folder}")

try:
    while True:
        time.sleep(10)  # Keep the script running
except KeyboardInterrupt:
    print("Stopping observer...")
    observer.stop()

observer.join()
