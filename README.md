AI Voice Assistant (Desktop Automation Bot)

A powerful Python-based Voice Assistant that can listen, speak, automate system tasks, and perform smart searches. This assistant acts like your personal desktop companion and responds to voice commands in real-time.

🚀 Features

🧠 Smart AI Responses
Answers questions using Wikipedia
Falls back to Google search if no result is found

🎤 Voice Interaction

Speech Recognition (Google API)
Text-to-Speech using pyttsx3
Stop speaking instantly with "stop" command

💻 System Automation

Mouse control (move, click, double click)
Keyboard automation (type, enter)
Volume control (up, down, mute)
Window switching (Alt + Tab)
Take screenshots
Lock screen

📂 Application Control

Open Notepad
Open Chrome
🌐 Web Features

Google search
YouTube search

🎵 Entertainment

Play random music from system
Tell jokes

💬 Communication

Send WhatsApp messages using pywhatkit

🛠️ Tech Stack

Python 3.x
Speech Recognition (speech_recognition)
Text-to-Speech (pyttsx3)
Automation (pyautogui)

Web APIs:

Wikipedia
Google Speech API

📦 Installation

1. Clone the Repository
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
2. Install Dependencies
pip install pyttsx3 SpeechRecognition wikipedia pyjokes pywhatkit pyautogui pyaudio

⚠️ Note: Installing pyaudio may require additional setup on Windows.

▶️ Usage

Run the script:

python assistant.py
🗣️ Activation Command

Say:

Hey Buddy
🔥 Example Commands
"Who is Elon Musk"
"Open Chrome"
"Play music"
"Take screenshot"
"Volume up"
"Send WhatsApp message"
"Tell me a joke"
"What is Artificial Intelligence"

❌ Exit Commands

"Goodbye"
"Exit"
"Quit"

📁 Project Structure

voice-assistant/
│── assistant.py
│── README.md

⚙️ Key Functional Modules


speak() → Converts text to speech
listen_me() → Captures voice input
smart_answer() → Fetches AI responses
send_whatsapp_message() → Sends messages
take_screenshot() → Saves screenshot to Desktop
control_mouse() → Automates cursor

⚠️ Limitations

Requires internet for speech recognition & Wikipedia
Works best in low-noise environments
Hardcoded paths (e.g., Music folder)
Windows-specific commands (sapi5, rundll32)

🔮 Future Improvements

Add ChatGPT API integration
Face/voice authentication
GUI dashboard
Multi-language support
Custom wake word detection

🤝 Contributing

Feel free to fork this repo and improve the assistant with new features.

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Ashin R
AI & Data Science Student
Passionate about building real-world AI projects 🚀
