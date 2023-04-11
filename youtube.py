import pywhatkit as pwt
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


pwt.playonyt("Python for beginners")