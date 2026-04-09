import pyautogui

def click(x=None, y=None):
    try:
        if x is not None and y is not None:
            pyautogui.click(x, y)
        else:
            pyautogui.click()
        return "Mouse clicked"
    except Exception as e:
        print("[Mouse Error]:", e)
        return None


def move(x, y):
    try:
        pyautogui.moveTo(x, y, duration=0.5)
        return f"Moved mouse to {x},{y}"
    except Exception as e:
        print("[Mouse Error]:", e)
        return None


def scroll(amount):
    try:
        pyautogui.scroll(amount)
        return f"Scrolled {amount}"
    except Exception as e:
        print("[Mouse Error]:", e)
        return None