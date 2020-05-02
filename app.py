import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
    print(words)
    os.system("say " + words)

talk("Hi, ask me something")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="en-US").lower()
        talk("You said: " + task)
        #print("You said: " + task)
    except sr.UnknownValueError:
        talk("I didnt understand you")
        task = command()

    return task

def makeSomething(task):
    if "how are you" in task:
        talk("I am good, thank you igor")

    if "who is making coffee" in task:
        talk("It is Dmitri who likes to drink coffee")

    if "open robinhood" in task:
        talk("Opening")
        url = "https://www.robinhood.com"
        webbrowser.open(url)
    elif "stop" in task:
        talk("Sure")
        sys.exit()

while True:
    makeSomething(command())