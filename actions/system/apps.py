import subprocess

# ---------------------------
# DESKTOP APPS
# ---------------------------
DESKTOP_APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "vscode": "code",
    "vs code": "code",
    "explorer": "explorer.exe",
    "file explorer": "explorer.exe",
    "files": "explorer.exe",
    "spotify": "start spotify:",   # ✅ FIXED (better than .exe)
    "chrome": "start chrome",
    "paint": "mspaint.exe",
    "vlc": "vlc.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "task manager": "taskmgr.exe",
    "cmd": "cmd.exe",
}

# ---------------------------
# WEBSITES
# ---------------------------
WEBSITES = {
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "x": "https://www.x.com",
    "netflix": "https://www.netflix.com",
    "swiggy": "https://www.swiggy.com",
    "zomato": "https://www.zomato.com",
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "flipkart": "https://www.flipkart.com",
    "amazon": "https://www.amazon.in",
    "github": "https://www.github.com",
    "whatsapp": "https://web.whatsapp.com",
    "gmail": "https://www.gmail.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "hotstar": "https://www.hotstar.com",
    "prime": "https://www.primevideo.com",
    "chatgpt": "https://www.chatgpt.com",
    "lovable": "https://lovable.dev",
    "figma": "https://www.figma.com",
    "maps": "https://maps.google.com",
    "google maps": "https://maps.google.com",
    "paytm": "https://www.paytm.com",
    "phonepe": "https://www.phonepe.com",
    "bookmyshow": "https://www.bookmyshow.com",
    "irctc": "https://www.irctc.co.in",
    "myntra": "https://www.myntra.com",
    "meesho": "https://www.meesho.com",
    "nykaa": "https://www.nykaa.com",
    "ola": "https://www.olacabs.com",
    "uber": "https://www.uber.com",
}


# ---------------------------
# NORMALIZE INPUT
# ---------------------------
def normalize_name(name):
    return name.lower().replace("_", " ").strip()


# ---------------------------
# MAIN FUNCTION
# ---------------------------
def open_app(name):
    name_lower = normalize_name(name)

    # ---------------------------
    # WEBSITE MATCH
    # ---------------------------
    if name_lower in WEBSITES:
        try:
            from actions.browser.web import open_url
            url = WEBSITES[name_lower]
            open_url(url)
            print(f"[Apps]: Opened {name_lower} in browser")
            return f"Opened {name_lower}"
        except Exception as e:
            print(f"[Apps Error]: {e}")
            return None

    # ---------------------------
    # DESKTOP APP MATCH
    # ---------------------------
    if name_lower in DESKTOP_APPS:
        try:
            cmd = DESKTOP_APPS[name_lower]
            subprocess.Popen(cmd, shell=True)
            print(f"[Apps]: Opened {name_lower}")
            return f"Opened {name_lower}"
        except Exception as e:
            print(f"[Apps Error]: {e}")
            return None

    # ---------------------------
    # PARTIAL MATCH (SMART)
    # ---------------------------
    for key in DESKTOP_APPS:
        if key in name_lower:
            try:
                subprocess.Popen(DESKTOP_APPS[key], shell=True)
                print(f"[Apps]: Opened {key} (matched)")
                return f"Opened {key}"
            except:
                pass

    for key in WEBSITES:
        if key in name_lower:
            try:
                from actions.browser.web import open_url
                open_url(WEBSITES[key])
                print(f"[Apps]: Opened {key} (matched)")
                return f"Opened {key}"
            except:
                pass

    # ---------------------------
    # FALLBACK
    # ---------------------------
    try:
        subprocess.Popen(name, shell=True)
        print(f"[Apps]: Tried opening {name}")
        return f"Tried opening {name}"
    except Exception as e:
        print(f"[Apps Error]: {e}")
        return None