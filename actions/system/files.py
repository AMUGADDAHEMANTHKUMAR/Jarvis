import shutil
import os
import requests

def copy_file(source, destination):
    try:
        shutil.copy2(source, destination)
        print(f"[Files]: Copied {source} to {destination}")
        return f"Copied {source} to {destination}"
    except Exception as e:
        print(f"[Files Error]: {e}")
        return None

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"[Files]: Moved {source} to {destination}")
        return f"Moved {source} to {destination}"
    except Exception as e:
        print(f"[Files Error]: {e}")
        return None

def delete_file(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        print(f"[Files]: Deleted {path}")
        return f"Deleted {path}"
    except Exception as e:
        print(f"[Files Error]: {e}")
        return None

def list_files(path="."):
    try:
        files = os.listdir(path)
        print(f"[Files]: {files}")
        return ", ".join(files)
    except Exception as e:
        print(f"[Files Error]: {e}")
        return None

def download_file(url, destination=None):
    try:
        if not destination:
            filename = url.split("/")[-1] or "downloaded_file"
            destination = os.path.join(os.path.expanduser("~"), "Downloads", filename)
        response = requests.get(url, stream=True, timeout=30)
        with open(destination, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"[Files]: Downloaded to {destination}")
        return f"Downloaded to {destination}"
    except Exception as e:
        print(f"[Files Error]: {e}")
        return None
