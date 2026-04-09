import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Jarvis: Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("Jarvis: No speech detected")
            return None
        except sr.UnknownValueError:
            print("Jarvis: Could not understand")
            return None
        except Exception as e:
            print(f"[Listener Error]: {e}")
            return None