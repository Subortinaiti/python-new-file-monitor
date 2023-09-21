from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self, paths_to_ignore):
        self.paths_to_ignore = paths_to_ignore

    def should_ignore(self, path):
        for ignore_path in self.paths_to_ignore:
            if path.startswith(ignore_path):
                return True
        return False

    def on_created(self, event):
        if not event.is_directory and not self.should_ignore(event.src_path):
            print(f"New file created: {event.src_path}")
            with open("log.txt","a") as file:
                file.write(f"New file created: {event.src_path}")
                file.write("\n")

paths_to_ignore = [
    "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\",
    "C:\\Users\\User\\AppData\\Local\\Temp\\", #dangerously broad, might change
    "C:\\$Recycle.Bin\\", 
    "C:\\ProgramData\\USOPrivate\\UpdateStore\\",
    "C:\\Windows\\", #dangerously broad, might change
    "C:\\Users\\User\\AppData\\Local\\Razer\\",
    "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\", #dangerously broad, might change
    "C:\\Users\\User\\AppData\\Local\\NVIDIA Corporation\\",
    "C:\\Users\\User\\AppData\\Local\\Packages\\",
    "C:\\ProgramData\\USOShared\\Logs\\System\\",
    "C:\\ProgramData\\NVIDIA Corporation\\nvtopps\\",
    "C:\\ProgramData\\USOShared\\Logs\\System\\",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Scans\\",
    "C:\\ProgramData\\Razer\\",
    "C:\\Users\\User\\AppData\\Local\\Adobe\\",
    "C:\\Program Files (x86)\\Razer\\"
    ]
print("starting newfile monitoring")
event_handler = MyHandler(paths_to_ignore)
observer = Observer()
observer.schedule(event_handler, path="C:\\", recursive=True)
observer.start()

try:
    observer.join()
except KeyboardInterrupt:
    observer.stop()

observer.join()
