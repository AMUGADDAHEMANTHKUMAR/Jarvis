from actions.browser import open_youtube

COMMANDS = {}

def register(name, func):
    COMMANDS[name] = func

# register commands
register("open_youtube", open_youtube)