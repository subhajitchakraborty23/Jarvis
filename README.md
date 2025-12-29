# Jarvis
Jarvis is a Python-based voice assistant that listens to your commands, speaks responses using text-to-speech, and performs smart actions like opening websites, playing music, and answering questions using Google Gemini AI. It supports continuous speech recognition, command execution, and conversational replies, making it a real personal assistant.
🧠 Jarvis – AI Voice Assistant

Jarvis is a Python-based voice assistant that listens to your commands, speaks responses using text-to-speech, performs smart automation like opening websites and playing music, and answers questions using Google Gemini AI.
It works completely through voice, making it feel like your own personal AI companion on your computer.

🚀 Features

🎤 Listens to your voice commands

🗣️ Speaks responses using pyttsx3

🤖 Uses Google Gemini AI for intelligent conversation

🌍 Opens websites like Google, YouTube, Facebook, LinkedIn

🎵 Plays songs from a custom music library

🛑 Supports “Stop / Exit / Quit” to shut down Jarvis

🔐 Robust error handling for internet & mic failures

♻️ Continuous command loop

🛠️ Tech Stack

Python

SpeechRecognition

Pyttsx3 (Text-to-Speech)

Google GenAI

Webbrowser

Custom Music Library

📂 Project Structure
Jarvis/
│
├── jarvis.py          # Main assistant program
├── musiclibrary.py    # Song list + YouTube URLs
└── README.md

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/YOUR-USERNAME/Jarvis.git
cd Jarvis

2️⃣ Install Required Packages
pip install speechrecognition
pip install pyttsx3
pip install google-genai
pip install pyaudio


If PyAudio fails on Windows:

pip install pipwin
pipwin install pyaudio


For speaking support on Windows:

pip install pywin32

🔑 Google Gemini Setup

1️⃣ Open Google AI Studio
https://aistudio.google.com

2️⃣ Generate an API Key

3️⃣ Add your key in the code:

GEMINI_API_KEY = "YOUR_REAL_GEMINI_KEY"

▶️ Run Jarvis
python jarvis.py


Jarvis will greet you:

“Hey sir, how may I help you?”

Now try commands like:

open google

open youtube

open facebook

play despacito

who is elon musk

what is quantum tunneling

quit / stop / exit

🎶 Music Library

Edit musiclibrary.py like this:

music = {
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "alone": "https://youtu.be/1-xGerv5FOk"
}

🧯 Troubleshooting
❌ Jarvis not speaking?

Force Windows TTS driver:

engine = pyttsx3.init('sapi5')


Ensure:

pip install pywin32

❌ Jarvis speaks only once?

Use threaded TTS

Ensure microphone permissions

Catch timeout errors

🔮 Future Improvements

🔔 Wake Word (“Hey Jarvis”)

🖥️ System Controls (apps, volume, brightness)

⏰ Reminders & alarms

🌦 Weather & news support

🧠 Memory-based conversations

🎨 GUI Version

❤️ Credits

Built with:

Python

Google Gemini AI

SpeechRecognition

Pyttsx3
