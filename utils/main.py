import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 定义要监测的文件夹路径
folder_to_watch = "."

# 从hot_load.txt中读取要监测的文件列表
whitelist = []
with open('hot_load.txt', 'r') as file:
    whitelist = file.read().splitlines()

# 定义要执行的命令
hexo_command = "hexo s"

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if any(filename in event.src_path for filename in whitelist):
            print("Detected change in whitelisted file. Restarting Hexo...")
            restart_hexo()

def restart_hexo():
    try:
        # 停止hexo服务
        subprocess.run(["pkill", "-f", "hexo s"])
        # 启动hexo服务
        subprocess.Popen(hexo_command.split(), cwd=folder_to_watch)
    except Exception as e:
        print(f"Error restarting Hexo: {e}")

if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)
    observer.start()
    print(f"Watching folder {folder_to_watch} for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
