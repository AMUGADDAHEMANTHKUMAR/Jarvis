import pyautogui
import time

def type_text(text, delay=0.05):
    try:
        time.sleep(0.5)
        pyautogui.write(text, interval=delay)
        return f"Typed: {text}"
    except Exception as e:
        print(f"[Keyboard Error]: {e}")
        return None

def press_key(key):
    try:
        pyautogui.press(key)
        return f"Pressed {key}"
    except Exception as e:
        print(f"[Keyboard Error]: {e}")
        return None

def hotkey(*keys):
    try:
        pyautogui.hotkey(*keys)
        return f"Hotkey: {keys}"
    except Exception as e:
        print(f"[Keyboard Error]: {e}")
        return None
