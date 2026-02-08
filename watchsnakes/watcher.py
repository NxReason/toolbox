import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

class DirHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent) -> None:
        print(event.event_type, event.src_path)

def watch(path: str = '.'):
    if os.path.exists(path):
        print('path is valid')
    else: return
    event_handler = DirHandler()
    observer = Observer()
    
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print(f'Watching: {path}')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    watch('/home/nxr/Dev/toolbox')
