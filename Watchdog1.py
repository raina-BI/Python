import os
import shutil
import time
import magic

# filesystemeventhandler  observer class of watchdog module
# look for changes in the path mentioned, and calls the specific event handler

from watchdog.observers import Observer 
# event handler class that manages the file system events(eg creation, movement, deletion)
from watchdog.events import FileSystemEventHandler

# paths

from_dir = "C:/Users/raina/Downloads"
to_dir = "C:/Users/raina/Desktop"


dir_tree={
    "Image_files":[".jpg",".jpeg",".png"],
    "Video_files":[".mp4",".mp3",".mov",".avi"],
    "Document_files":[".ppt",".csv",".pdf",".txt"]
}

# Creating class FileMovementHandler and pass FileSystemEventHandler as parameter to use all the methods and attributes from FileSystemEventHandler inside FileMovementHandler
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)

        time.sleep(2)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("Downloaded"+file_name)

                path1= from_dir+ '/'+file_name
                path2=to_dir+'/'+key
                path3=to_dir + '/'+key +'/'+file_name

                if os.path.exists(path2):
                    print("Directory exists..")
                    print("moving"+ file_name+ "...")
                    shutil.move(path1,path3)
                    print( file_name+" moved"+"...")
                    time.sleep(1)
                else:
                  print("Making Directory..")
                  os.makedirs(path2)
                  print("Moving"+file_name+ "...")
                  shutil.move(path1,path3)
                  time.sleep(1)
            elif extension == '':
                file_type = magic.from_file(path1,mime=True)
                print(f"File type: {file_type}")

                path1= from_dir+ '/'+file_name
                path2=to_dir+'/'+key
                path3=to_dir + '/'+key +'/'+file_name

                if os.path.exists(path2):
                    print("Directory exists..")
                    print("moving"+ file_name+ "...")
                    shutil.move(path1,path3)
                    print( file_name+" moved"+"...")
                    time.sleep(1)
                else:
                  print("Making Directory..")
                  os.makedirs(path2)
                  print("Moving"+file_name+ "...")
                  shutil.move(path1,path3)
                  time.sleep(1)

  # intialize event handler class                
event_handler  = FileMovementHandler()
observer=Observer()
#recursive=true observe the changes in subfolders as well
observer.schedule(event_handler, from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(30)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
