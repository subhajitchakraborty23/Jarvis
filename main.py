import webbrowser
import speech_recognition as sr
import pyttsx3
import musiclibrary
import requests
from google import genai


# ---------------- INITIAL SETUP ----------------
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

GEMINI_API_KEY = "AIzaSyA0NSskv46S4jp2ekhEAanwzFvJWmg85DY"
client = genai.Client(api_key=GEMINI_API_KEY)
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return "Sorry sir, Gemini is not responding."

def process_command(text):
    text_lower = text.lower()
    if "open google" in text_lower:
        webbrowser.open("https://google.com")
    elif "open facebook" in text_lower:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in text_lower:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in text_lower:
        webbrowser.open("https://linkedin.com")
    elif text_lower.startswith("play"):
        song = text_lower.split(" ")[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in your music library.")
    else:
        # Send unrecognized commands to Gemini
        reply = ask_gemini(text)
        speak(reply)

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    speak("Hey sir, how may I help you?")

    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=10, phrase_time_limit=5)

            text = r.recognize_google(audio)
            print("You said:", text)

            # Check for exit commands
            if any(word in text.lower() for word in ["stop", "exit", "quit"]):
                speak("Goodbye Sir!")
                break

            process_command(text)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results; check internet connection.", e)
