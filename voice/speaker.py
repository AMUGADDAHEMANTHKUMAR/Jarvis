import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 0.9)

def speak(text):
    try:
        print(f"Jarvis speaks: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"[Speaker Error]: {e}")