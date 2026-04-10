# import json

# ALLOWED_PATHS = [
#     "system.open_app",
#     "system.run_command",
#     "system.copy_file",
#     "system.move_file",
#     "system.delete_file",
#     "system.list_files",
#     "system.download_file",
#     "browser.youtube.search",
#     "browser.youtube.open",
#     "browser.web.open_url",
#     "browser.web.open",
#     "browser.web.search_on_page",
#     "automation.keyboard.type_text",
#     "automation.keyboard.press_key",
#     "automation.keyboard.hotkey",
#     "media.spotify.search_song",
#     "media.spotify.open_app",
#     "media.spotify.open",
#     "media.spotify.play_song",
#     "media.spotify.play_paused_song",
#     "git.clone",
#     "git.open_in_vscode",
# ]

# def validate(raw):
#     try:
#         raw = raw.strip()
#         start_list = raw.find("[")
#         start_obj = raw.find("{")

#         if start_list != -1 and (start_obj == -1 or start_list < start_obj):
#             clean = raw[start_list:raw.rfind("]")+1]
#             items = json.loads(clean)
#             valid = []
#             for item in items:
#                 path = item.get("path")
#                 if path in ALLOWED_PATHS:
#                     if "args" not in item:
#                         item["args"] = {}
#                     valid.append(item)
#                     print(f"[Validator]: Approved step: {path}")
#                 else:
#                     print(f"[Validator]: Skipping unknown: {path}")
#             return valid if valid else None

#         if start_obj == -1:
#             print("[Validator]: No JSON found")
#             return None

#         clean = raw[start_obj:raw.rfind("}")+1]
#         cmd = json.loads(clean)

#         if "path" not in cmd:
#             return None
#         if cmd["path"] not in ALLOWED_PATHS:
#             print(f"[Validator]: Unknown path: {cmd['path']}")
#             return None
#         if "args" not in cmd:
#             cmd["args"] = {}
#         return cmd

#     except Exception as e:
#         print(f"[Validator Error]: {e}")
#         return None


import json

ALLOWED_PATHS = [
    "system.open_app",
    "system.run_command",
    "system.copy_file",
    "system.move_file",
    "system.delete_file",
    "system.list_files",
    "system.download_file",
    "browser.youtube.search",
    "browser.youtube.open",
    "browser.web.open_url",
    "browser.web.open",
    "browser.web.search_on_page",
    "automation.keyboard.type_text",
    "automation.keyboard.press_key",
    "automation.keyboard.hotkey",
    "media.spotify.search_song",
    "media.spotify.open_app",
    "media.spotify.open",
    "media.spotify.play_song",
    "media.spotify.play_paused_song",
    "git.clone",
    "git.open_in_vscode",
]

def validate(raw):
    try:
        raw = raw.strip()
        start_list = raw.find("[")
        start_obj = raw.find("{")

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

        if start_obj == -1:
            print("[Validator]: No JSON found")
            return None

        clean = raw[start_obj:raw.rfind("}")+1]
        cmd = json.loads(clean)

        if 'path' not in cmd:
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