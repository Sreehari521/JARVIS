import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import psutil
import webbrowser
import requests
import os

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

    elif 'turn off' in command or 'shut up' in command or 'stop' in command:
        talk("Okay sir")
        sys.exit()

    elif 'battery' in command:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        talk(f"Sir, your system have {percentage} percent battery")

    elif 'open google' in command:
        talk("Sure Sir")
        talk("Opening Google")
        webbrowser.open("http://www.google.com")
        talk("Job Done Sir")

    elif 'open youtube' in command:
        talk("Sure Sir")
        talk("Opening YouTube")
        webbrowser.open("http://www.youtube.com")
        talk("Job Done Sir")

    elif 'open scratch' in command:
        talk("Sure Sir")
        talk("Opening Scratch")
        webbrowser.open("http://scratch.mit.edu")
        talk("Job Done Sir")

    elif 'open notepad' in command:
        talk("Sure Sir")
        talk("Opening Notepad")
        os.startfile("C:/Windows/System32/notepad.exe")
        talk("Job Done Sir")

    elif 'open command prompt' in command or 'open cmd' in command:
        talk("Sure Sir")
        talk("Opening Command Prompt")
        os.system("start cmd")
        talk("Job Done Sir")

    elif 'where are we' in command or 'where am i' in command or 'where i am' in command or 'where we are' in command:
        talk("I am looking that Sir, please wait some seconds")
        try:
            ipAdr = requests.get("https://api.ipify.org").text
            print(ipAdr)
            url = "https://get.geojs.io/v1/ip/geo/" + ipAdr + '.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data["city"]
            country = geo_data["country"]
            print(f'Sir, I am not sure but I think that we are in the {city} city of {country}')
            talk(f'Sir, I am not sure but I think that we are in the {city} city of {country}')
        except Exception as e:
            talk("Sorry Sir, Because of some network issues or some other issues I can't find where we are.")

    else:
        talk("I don't understand that command")
        run()

while True:
    run()