import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import pywhatkit as kit
import pyautogui
import sys

# -------------------- GLOBAL STOP FLAG --------------------
stop_speaking = False


# -------------------- SPEAK FUNCTION --------------------
def speak(audio):
    global stop_speaking

    print("Assistant:", audio)

    sentences = audio.split(".")

    for sentence in sentences:
        if stop_speaking:
            stop_speaking = False
            break

        try:
            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate', 180)

            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)

            engine.say(sentence)
            engine.runAndWait()
            engine.stop()

        except Exception as e:
            print("TTS Error:", e)


# -------------------- GREETING --------------------
def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour < 12:
        speak("Good morning boss")
    elif hour < 18:
        speak("Good afternoon boss")
    else:
        speak("Good evening boss")

    speak("How can I help you?")


# -------------------- LISTEN FUNCTION --------------------
def listen_me():
    global stop_speaking

    r = sr.Recognizer()

    try:
        with sr.Microphone() as mic:
            print("Listening...")
            r.adjust_for_ambient_noise(mic, duration=1)
            audio = r.listen(mic, timeout=5, phrase_time_limit=5)

        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        query = query.lower()

        print("You said:", query)

        if "stop" in query:
            stop_speaking = True

        return query

    except:
        return ""


# -------------------- SMART ANSWER --------------------
def smart_answer(query):
    global stop_speaking

    try:
        speak("Searching for information")

        clean_query = query.replace("who is", "").replace("what is", "").replace("tell me about", "").strip()

        result = wikipedia.summary(clean_query, sentences=5)

        speak("Here is what I found")

        sentences = result.split(".")
        for sentence in sentences:
            if stop_speaking:
                speak("Stopping")
                stop_speaking = False
                break
            speak(sentence)

    except:
        speak("Couldn't find exact answer, opening Google")
        webbrowser.open(f"https://www.google.com/search?q={query}")


# -------------------- WHATSAPP --------------------
def send_whatsapp_message():
    speak("Please type the phone number with country code")
    number = input("Enter phone number: ").strip()

    if number:
        if not number.startswith("+"):
            number = "+" + number

        speak("What message should I send?")
        message = listen_me()

        if message:
            try:
                kit.sendwhatmsg_instantly(number, message, wait_time=10)
                speak("Message sent successfully")
            except:
                speak("Failed to send message")
        else:
            speak("Message not captured")
    else:
        speak("Number not entered")


# -------------------- MUSIC --------------------
def play_music():
    music_dir = "C:\\Users\\Public\\Music"

    if os.path.exists(music_dir):
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            speak("Playing music")
        else:
            speak("No songs found")
    else:
        speak("Music folder not found")


# -------------------- SYSTEM CONTROL --------------------
def control_mouse():
    pyautogui.moveTo(500, 500, duration=1)
    speak("Mouse moved")

def click_mouse():
    pyautogui.click()
    speak("Clicked")

def double_click():
    pyautogui.doubleClick()
    speak("Double clicked")

def type_text():
    speak("What should I type?")
    text = listen_me()
    if text:
        pyautogui.write(text, interval=0.05)
        speak("Typing completed")

def press_enter():
    pyautogui.press("enter")
    speak("Pressed enter")

def volume_up():
    pyautogui.press("volumeup")
    speak("Volume increased")

def volume_down():
    pyautogui.press("volumedown")
    speak("Volume decreased")

def mute_volume():
    pyautogui.press("volumemute")
    speak("Muted")

def switch_window():
    pyautogui.hotkey("alt", "tab")
    speak("Switching window")

def take_screenshot():
    try:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop, "screenshot.png")

        img = pyautogui.screenshot()
        img.save(file_path)

        print("Saved at:", file_path)
        speak("Screenshot taken and saved on desktop")

    except Exception as e:
        print("Screenshot error:", e)
        speak("Failed to take screenshot")

def lock_screen():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def open_notepad():
    os.system("notepad")
    speak("Opening Notepad")

def open_chrome():
    os.system("start chrome")
    speak("Opening Chrome")


# -------------------- MAIN PROGRAM --------------------
if __name__ == "__main__":
    wishme()

    while True:
        query = listen_me()

        if query == "":
            continue

        # -------- WAKE WORD --------
        if "hey" in query or "buddy" in query:
            speak("Yes boss, I am listening")

            while True:
                query = listen_me()

                if query == "":
                    continue

                # -------- EXIT (FULL STOP) --------
                if "exit" in query or "goodbye" in query:
                    speak("Goodbye boss")
                    sys.exit()

                # -------- SMART SEARCH --------
                elif "who is" in query or "what is" in query or "tell me about" in query:
                    smart_answer(query)

                # -------- SYSTEM CONTROL --------
                elif "move mouse" in query:
                    control_mouse()

                elif "click" in query:
                    click_mouse()

                elif "double click" in query:
                    double_click()

                elif "type" in query:
                    type_text()

                elif "enter" in query:
                    press_enter()

                elif "volume up" in query:
                    volume_up()

                elif "volume down" in query:
                    volume_down()

                elif "mute" in query:
                    mute_volume()

                elif "switch window" in query:
                    switch_window()

                elif "screenshot" in query:
                    take_screenshot()

                elif "lock screen" in query:
                    lock_screen()

                elif "open notepad" in query:
                    open_notepad()

                elif "open chrome" in query:
                    open_chrome()

                # -------- OTHER FEATURES --------
                elif "google" in query:
                    speak("What should I search?")
                    search = listen_me()
                    webbrowser.open(f"https://www.google.com/search?q={search}")

                elif "youtube" in query:
                    speak("What should I search on YouTube?")
                    search = listen_me()
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

                elif "play music" in query:
                    play_music()

                elif "whatsapp" in query:
                    send_whatsapp_message()

                elif "joke" in query:
                    speak(pyjokes.get_joke())

                elif "time" in query:
                    time_now = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {time_now}")

                elif "stop" in query:
                    stop_speaking = True
                    speak("Stopped")
                    sys.exit()



                else:
                    speak("Searching on Google")
                    webbrowser.open(f"https://www.google.com/search?q={query}")

        # -------- OUTER EXIT --------
        elif "quit" in query:
            speak("Goodbye boss")
            sys.exit()

        else:
            speak("Say hey buddy to activate me")