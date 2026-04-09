import json

ALLOWED_PATHS = [
    "system.open_app",

    # ---------------------------
    # YOUTUBE
    # ---------------------------
    "browser.youtube.search",
    "browser.youtube.open",
    "browser.youtube.play",

    # ---------------------------
    # WEB
    # ---------------------------
    "browser.web.open_url",
    "browser.web.open",
    "browser.web.search",   # ✅ ADD THIS

    # ---------------------------
    # AUTOMATION
    # ---------------------------
    "automation.keyboard.type_text",

    # ---------------------------
    # SPOTIFY
    # ---------------------------
    "media.spotify.search_song",
    "media.spotify.open_app",
    "media.spotify.open",
    "media.spotify.play_song",
    "media.spotify.play_paused_song",
]


def validate(raw):
    try:
        raw = raw.strip()

        start_list = raw.find("[")
        start_obj = raw.find("{")

        # ---------------------------
        # MULTI COMMAND
        # ---------------------------
        if start_list != -1 and (start_obj == -1 or start_list < start_obj):
            clean = raw[start_list:raw.rfind("]")+1]
            items = json.loads(clean)

            valid = []
            for item in items:
                path = item.get('path')

                if path in ALLOWED_PATHS:
                    if 'args' not in item:
                        item['args'] = {}
                    valid.append(item)
                    print(f"[Validator]: Approved step: {path}")
                else:
                    print(f"[Validator]: Skipping unknown: {path}")

            return valid if valid else None

        # ---------------------------
        # SINGLE COMMAND
        # ---------------------------
        if start_obj == -1:
            print("[Validator]: No JSON found")
            return None

        clean = raw[start_obj:raw.rfind("}")+1]
        cmd = json.loads(clean)

        if 'path' not in cmd:
            print("[Validator]: Missing path key")
            return None

        if cmd['path'] not in ALLOWED_PATHS:
            print(f"[Validator]: Unknown path: {cmd['path']}")
            return None

        if 'args' not in cmd:
            cmd['args'] = {}

        return cmd

    except Exception as e:
        print(f"[Validator Error]: {e}")
        return None