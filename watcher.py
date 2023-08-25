from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import subprocess

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.proc = subprocess.Popen(['python', 'main.py'])
        self.observer = Observer()
        self.observer.schedule(self, path='.', recursive=True)

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f'File {event.src_path} has been modified, restarting script.')
            self.proc.terminate()
            self.proc = subprocess.Popen(['python', 'main.py'])

    def run(self):
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            self.proc.terminate()
        self.observer.join()

if __name__ == "__main__":
    handler = MyHandler()
    handler.run()