import pyautogui
import time

def type_text(text):
    try:
        pyautogui.write(text, interval=0.05)
        return f"Typed: {text}"
    except Exception as e:
        print("[Keyboard Error]:", e)
        return None


def press_key(key):
    try:
        pyautogui.press(key)
        return f"Pressed {key}"
    except Exception as e:
        print("[Keyboard Error]:", e)
        return None