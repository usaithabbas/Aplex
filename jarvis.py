import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes
from playsound import playsound
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning sir")
        speak("Good Morning sir")
    elif hour >= 12 and hour < 17:
        print("Good Afternoon sir")
        speak("Good Afternoon sir")
    elif hour >= 17 and hour < 21:
        print("Good Evening sir")
        speak("Good Evening sir")
    else:
        print("Good night sir")
        speak("Good night sir")

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("jarvis is ready to take command sir...")
        r.pause_thershold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Analyzing sir...")
        ques = r.recognize_google(audio, language='en-in')
        print(f"Abbas sir said: {ques}\n")

    except Exception as e:
        print(e)
        speak("Please Tell me again sir")
        ques = "can't recognize tell me again"
    return ques


def wakeupcommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am sleeping...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"Tony: {query}\n")
    except Exception as e:
        query = "none"
    return query


if __name__ == "__main__":
    while True:
        query = wakeupcommands().lower()
        if "wake up" in query or 'wake' in query:
            wishings()
            speak("Yes sir what can i do for you!")
            while True:

                query = commands().lower()
                if 'search' in query or 'wikipedia' in query:
                    speak("searching sir...")
                    try:
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=1)
                        speak("According to our search,")
                        print(results)
                        speak(results)
                    except:
                        speak("No results found....")
                        print("No results found....")

                elif 'thanks' in query or 'superb' in query or 'okay' in query:
                    speak("Your welcome sir!!!")

                elif 'No' in query:
                    speak("okay sir!!!")
                    print('okay sir!!!')

                elif 'your boss name' in query or 'who is your boss' in query or 'who i am' in query:
                    speak("My Boss name is S.Mohammed Usaith abbas he is my tony stark and i am him jarvis.")
                    print("My Boss name is S.Mohammed Usaith abbas he is my tony stark and i am him jarvis.")

                elif 'what can your boss do' in query or 'who is Mohammed usaith abbas' in query or 'what is your boss is doing' in query:
                    speak("My Boss S.Mohammed Usaith abbas. he is a full stack web developer and a app developer. he is also good at python and i am his first project in python. and he also running a youtube channel name codex. Do you like to visit his channek? .")
                    print("My Boss S.Mohammed Usaith abbas. he is a full stack web developer and a app developer. he is also good at .python ana i am his first project in python. and he also running a youtube channel name codex. Do you like to visit his channel?.")

                elif 'time' in query or 'what is the time now' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)
                    speak(f"Sir,the time is {strTime}")

                elif 'type' in query:
                    speak("Please tell me what should i write")
                    while True:
                        writeInNotepad = commands()
                        if writeInNotepad == 'exit typing':
                            speak("Done Sir!")
                            break
                        else:
                            pyautogui.write(writeInNotepad)


                elif 'wake up' in query:
                    wishings()
                    print("What can i do for you?")
                    speak("What can i do for you?")

                elif 'maximize' in query or 'maximise' in query:
                    speak("maximizing sir..")
                    pyautogui.hotkey('win', 'up', 'up')

                elif 'minimize' in query or 'minimise' in query:
                    speak("minimizing sir..")
                    pyautogui.hotkey('win', 'down', 'down')


                elif 'open chrome' in query or 'open google' in query:
                    speak("opening Chrome Application Sir...")
                    os.startfile("C:\Program Files\Google\Chrome\Application\Chrome.exe")


                elif "close chrome" in query or "exit Chrome" in query:
                    pyautogui.hotkey('ctrl', 'w')
                    speak("Closing google chrome sir!!!")


                elif 'open vs code' in query or 'open code' in query:
                    speak("opening vs code Application Sir...")
                    os.startfile("C:\Program Files (x86)\Microsoft VS Code\Code.exe")

                elif "close application" in query or "exit app" in query:
                    pyautogui.hotkey('ctrl', 'w')
                    speak("Closing application sir!!!")


                    while True:
                        chromeQuery = commands().lower()
                        if "search" in chromeQuery:
                            youtubeQuery = chromeQuery
                            youtubeQuery = youtubeQuery.replace("search", "")
                            pyautogui.write(youtubeQuery)
                            pyautogui.press('enter')
                            speak('searching...')

                        elif "close chrome" in chromeQuery or "exit Chrome" in chromeQuery:
                            pyautogui.hotkey('ctrl', 'w')
                            speak("Closing google chrome sir!!!")
                            break


                elif 'play' in query:
                    query = query.replace('play', '')
                    speak('playing' + query)
                    pywhatkit.playonyt(query)

                elif "mute" in query:
                    speak("I am Muting sir...")
                    break

                elif "love" in query:
                    speak("yes sir, I love You too.")

                elif "good job" in query:
                    speak("yes sir, My pleasure.")

                elif "magic sentence" in query:
                    speak("yes sir, for your pleasure")
                    speak("You are the real life tony Stark")

                elif "what can you do for me" in query:
                    speak("yes sir!, nice question")
                    speak("As my program, I'm a bot which can perform tasks through your voice control.")

                elif "cool" in query or 'nice' in query or 'awesome' in query:
                    speak("yes sir, My pleasure")

                elif 'close window' in query or 'close the application' in query:
                    pyautogui.hotkey('ctrl', 'w')
                    speak('closing sir')


                elif 'screenshot' in query:
                    speak('Taking screenshot sir')
                    pyautogui.hotkey('prtsc')


                elif 'notepad' in query or 'open Notepad' in query:
                    speak("opening notepad sir")
                    os.startfile('C:\\Windows\\system32\\notepad.exe')

                elif 'paste' in query:
                            pyautogui.hotkey('ctrl', 'v')
                            speak('done sir')

                elif 'save this file' in query or 'save' in query:
                            pyautogui.hotkey('ctrl', 's')
                            speak('Sir, please specify a name for this file')
                            notepadsavingquery = commands()
                            pyautogui.write(notepadsavingquery)
                            pyautogui.press('enter')

                elif 'exit notepad' in query or 'close notepad' in query:
                            speak('closing notepad sir')
                            pyautogui.hotkey('ctrl', 'w')

                elif 'joke' in query:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)

                elif 'alarm' in query:
                    speak("enter the timer sir:")
                    time = input("enter the time:")

                    while True:
                        time_at = datetime.datetime.now()
                        now = time_at.strftime("%H:%M:%S")

                        if now == time:
                            speak("time to wake up sir!!!")
                            playsound('iron_man_back_in.mp3')
                            speak('alarm Closed')
                            break

                elif 'shut down' in query or 'shut' in query:
                    speak('shutting down your system sir')
                    pyautogui.hotkey('alt', 'f4')


                elif 'music' in query or 'play music' in query or 'play a song' in query:
                    speak("yes sir please wait a moment...")
                    songs=os.listdir('E:\\New folder\Playlists\Playlists')
                    os.startfile(os.path.join('E:\\New folder\Playlists\Playlists'))

                elif 'pause' in query or 'resume' in query:
                    pyautogui.press('space')
                    speak('Done sir...')

                elif 'select all' in query:
                    speak("selected all sir")
                    pyautogui.hotkey('ctrl', 'a')

                elif 'copy' in query:
                    pyautogui.hotkey('ctrl', 'c')
                    speak('the selected text has been copied sir')

                elif 'date' in query:
                    strdate = datetime.datetime.now().strftime('%B %d, /20%y')
                    print(f"Today is: {strdate}")
                    speak(f"Today is, {strdate}")

                elif 'which day it is' in query or 'what is the day today' in query or 'day' in  query:
                    day = datetime.datetime.today().weekday() + 1
                    day_dict = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday",
                                7: "sunday"}

                    if day in day_dict.keys():
                        day_of_the_week = day_dict[day]
                        print("Sir Today is " + day_of_the_week)
                        speak('Sir Today is ' + day_of_the_week)

