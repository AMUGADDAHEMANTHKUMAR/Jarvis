import subprocess
import pyautogui
import time
import pygetwindow as gw

def open_spotify():
    try:
        subprocess.Popen("spotify.exe", shell=True)
        time.sleep(4)
        # bring spotify to front
        try:
            windows = gw.getWindowsWithTitle("Spotify")
            if windows:
                windows[0].activate()
                time.sleep(0.5)
        except:
            pass
        return "Opened Spotify"
    except Exception as e:
        print("[Spotify Error]:", e)
        return None

def search_song(query):
    try:
        open_spotify()
        time.sleep(2)

        # bring spotify to front
        try:
            windows = gw.getWindowsWithTitle("Spotify")
            if windows:
                windows[0].activate()
                time.sleep(0.5)
        except:
            pass

        # click search box
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.8)

        # type query
        pyautogui.hotkey("ctrl", "a")
        pyautogui.write(query, interval=0.05)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(2.5)

        # press Tab to focus first result then Enter to play
        pyautogui.press("tab")
        time.sleep(0.3)
        pyautogui.press("tab")
        time.sleep(0.3)
        pyautogui.press("tab")
        time.sleep(0.3)
        pyautogui.press("enter")
        time.sleep(0.5)

        return f"Searched and playing {query} on Spotify"

    except Exception as e:
        print("[Spotify Error]:", e)
        return None

def play_song():
    try:
        try:
            windows = gw.getWindowsWithTitle("Spotify")
            if windows:
                windows[0].activate()
                time.sleep(0.5)
        except:
            pass
        pyautogui.press("space")
        return "Playing song on Spotify"
    except Exception as e:
        print("[Spotify Error]:", e)
        return None

def open_spotify_and_play():
    try:
        open_spotify()
        time.sleep(1)
        pyautogui.press("space")
        return "Opened Spotify and playing"
    except Exception as e:
        print("[Spotify Error]:", e)
        return None