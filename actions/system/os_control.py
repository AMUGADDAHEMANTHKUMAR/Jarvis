import subprocess
import os

def run_command(command, cwd=None):
    try:
        print(f"[Terminal]: Running: {command}")
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=cwd or os.getcwd(),
            timeout=60
        )
        output = result.stdout.strip() or result.stderr.strip()
        print(f"[Terminal Output]: {output}")
        return output or "Command executed"
    except subprocess.TimeoutExpired:
        return "Command timed out"
    except Exception as e:
        print(f"[Terminal Error]: {e}")
        return None
