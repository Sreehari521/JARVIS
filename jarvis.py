import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import psutil

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        run()
    return command

def run():
    command = take_command()
    print(command)

    if 'hi' in command or 'hai' in command:
        talk("Hello Sir")

    if 'hello' in command:
        talk("Hi Sir")

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Sir, the current time is ' + time)

    elif 'thanks' in command or 'thank you' in command:
        talk('It is my job sir')

    elif 'how are you' in command or 'how is it going' in command:
        talk('Fine Sir, thanks for asking')

    elif 'tell me about' in command:
        info1 = command.replace('tell me about', '')
        info = wikipedia.summary(info1, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'hey jarvis' in command:
        talk("JARVIS is ready to serve you, sir!")

    elif 'who am i' in command:
        talk("You are my great boss! Sreehari")

    elif 'who are you' in command:
        talk("I am JARVIS, your personal assistant")

    elif 'good morning' in command:
        talk("Good morning sire, welcome to the computer")

    elif 'good night' in command:
        talk("Good bye sir, see you tomorrow")

    elif 'turn off' in command:
        talk("Okay sir")
        sys.exit()

    elif 'battery' or 'battery percentage' in command:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        talk(f"Sir, your system have {percentage} percent battery")

    else:
        run()

while True:
    run()