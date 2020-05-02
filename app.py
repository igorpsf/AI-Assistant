import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
    print(words)
    os.system("say " + words)

talk("Hi ")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk("Please ask me something")
        #print("Please ask me something else")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="en-US").lower()
        talk("You said: " + task)
        #print("You said: " + task)
    except sr.UnknownValueError:
        talk("I did not understand you")
        task = command()

    return task

def makeSomething(task):
    if "how are you" in task:
        talk("I am good, thank you igor")

    if "what is your name" in task:
        talk("I am AI assistant")

    if "what are you doing" in task:
        talk("I am talking with you and drinking orange juice")

    if "open robin hood" in task:
        talk("Opening")
        url = "https://www.robinhood.com"
        webbrowser.open(url)

    elif "stop" in task:
        talk("Sure, bye bye")
        sys.exit()

while True:
    makeSomething(command())