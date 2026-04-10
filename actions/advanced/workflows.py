import subprocess
import os
from actions.system.os_control import run_command

def git_clone(repo_url, destination=None):
    try:
        if not destination:
            destination = os.path.join(os.path.expanduser("~"), "Documents")
        cmd = f"git clone {repo_url}"
        result = run_command(cmd, cwd=destination)
        print(f"[Git]: Cloned {repo_url} to {destination}")
        return f"Cloned {repo_url}"
    except Exception as e:
        print(f"[Git Error]: {e}")
        return None

def open_in_vscode(path=None):
    try:
        if not path:
            path = "."
        run_command(f"code {path}")
        return f"Opened {path} in VS Code"
    except Exception as e:
        print(f"[VSCode Error]: {e}")
        return None
