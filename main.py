from brain.llm_engine import think   # ✅ FIXED
from brain.prompt_builder import build_prompt
# from brain.validator import validate
from brain.intent_parser import validate 
from actions.core.executor import execute
from voice.speaker import speak
from voice.listener import listen
import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_for_wake_word():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = recognizer.listen(source, timeout=6, phrase_time_limit=5)
            text = recognizer.recognize_google(audio).lower()
            print(f"[Wake]: Heard: {text}")
            return text
        except:
            pass
    return ""

def run_command(user_input):
    user_input = user_input.strip()
    if not user_input:
        return

    print(f"\nYou: {user_input}")

    prompt = build_prompt(user_input)
    raw = think(prompt)

    if not raw:
        speak("Sorry I could not connect to my brain")
        return

    print("[LLM RAW]:", raw)

    cmd = validate(raw)

    if not cmd:
        speak("Sorry I did not understand that command")
        return

    try:
        from actions.browser import web
        if web.driver:
            try:
                _ = web.driver.title
            except:
                web.driver = None
    except:
        pass

    if isinstance(cmd, list):
        print(f"[Jarvis]: Executing {len(cmd)} steps")
    else:
        print(f"[Jarvis]: Executing {cmd.get('path')}")

    result = execute(cmd)

    speak(str(result) if result else "Done")

if __name__ == "__main__":
    print("=" * 50)
    print("JARVIS IS ONLINE")
    print("Say '1' or 'Jarvis' → wake up in voice mode")
    print("Say '2' or 'Jarvis text' → wake up in text mode")
    print("Say '3' or 'Jarvis exit' → shut down")
    print("=" * 50)

    speak("Jarvis offline. Say 1 to speak, 2 to type, 3 to exit.")
    print("\n[Sleeping... waiting for wake word]")

    mode = "voice"

    while True:
        try:
            wake_text = listen_for_wake_word()

            if not wake_text:
                continue

            if any(w in wake_text for w in ["one", "1", "jarvis"]) and "two" not in wake_text and "text" not in wake_text:
                mode = "voice"
                speak("Jarvis online. Voice mode. I am listening.")
                print("\n[Jarvis AWAKE — VOICE mode]")
                break

            elif any(w in wake_text for w in ["two", "2", "text"]):
                mode = "text"
                speak("Jarvis online. Text mode. Type your commands.")
                print("\n[Jarvis AWAKE — TEXT mode]")
                break

            elif any(w in wake_text for w in ["three", "3", "exit", "stop"]):
                speak("Goodbye.")
                quit()

        except KeyboardInterrupt:
            quit()
        except:
            continue

    while True:
        try:
            if mode == "voice":
                print("\n[Voice Mode] Listening...")
                command = listen()

                if not command:
                    continue

                command_lower = command.lower()

                if any(w in command_lower for w in ["exit", "stop", "shutdown"]):
                    speak("Shutting down. Goodbye.")
                    break

                if any(w in command_lower for w in ["two", "text", "jarvis text"]):
                    mode = "text"
                    speak("Switching to text mode.")
                    print("\n[TEXT mode]")
                    continue

                run_command(command)

            elif mode == "text":
                print("\n[Text Mode] Type command:")
                print("  (type 'voice' or '1' to switch to voice, 'exit' to stop)")
                command = input(">> ").strip()

                if not command:
                    continue

                command_lower = command.lower()

                if any(w in command_lower for w in ["exit", "stop", "shutdown"]):
                    speak("Shutting down. Goodbye.")
                    break

                if command_lower in ["voice", "1", "speak", "jarvis speak"]:
                    mode = "voice"
                    speak("Switching to voice mode. I am listening.")
                    print("\n[VOICE mode]")
                    continue

                run_command(command)

        except KeyboardInterrupt:
            speak("Shutting down. Goodbye.")
            break
        except Exception as e:
            print(f"[Error]: {e}")
            continue