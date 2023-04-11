import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from tkinter import *
from PIL import ImageTk, Image
import pywhatkit as pwt
import openai
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import googletrans
import speech_recognition
import gtts
import playsound


root = Tk()
root.title("Debuggers")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#3e8187")

def yt():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("speak now")
        voice = recognizer.listen(source,0,8)
        text = recognizer.recognize_google(voice,language="hi")
        print(text)
    # print(googletrans.LANGUAGES)
        translator = googletrans.Translator()
        translation = translator.translate(text,dest="en")
    # print(translation.text)
        a = translation.text
        print(a)
        pwt.playonyt(a)

    

def cg():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("speak now")
        voice = recognizer.listen(source,0,8)
        text = recognizer.recognize_google(voice,language="hi")
        print(text)
    # print(googletrans.LANGUAGES)
        translator = googletrans.Translator()
        translation = translator.translate(text,dest="en")
    # print(translation.text)
        a = translation.text
        print(a)
        converted_audio = gtts.gTTS(translation.text, lang="en")
    # converted_audio.save("chatgpt.mp3")
    # playsound.playsound("hello.mp3")
    # music_dir = 'D:\\Jarvis Voice Assistant'
    # songs = os.listdir(music_dir)
    # print(songs)
    # os.startfile(os.path.join(music_dir, songs[7]))

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    openai.api_key="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"

    model_engine = "text-davinci-003"
    prompt = a

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n =1,
        stop = None,
        temperature = 0.5,
    )

    response = completion.choices[0].text
    print(response)
    # speak(response)

    # print(googletrans.LANGUAGES)
    translator = googletrans.Translator()
    translation = translator.translate(response,dest="hi")
    print(translation.text)
    converted_audio = gtts.gTTS(translation.text, lang="hi")
    converted_audio.save("chatgpt.mp3")
    # playsound.playsound("hello.mp3")
    music_dir = 'C:\\Users\\jaiam\\OneDrive\\Desktop\\New folder (4)\\Speech_Recoginition'
    songs = os.listdir(music_dir)
    # print(songs)
    os.startfile(os.path.join(music_dir, songs[4]))

def sleep():
    # speak("I am going for a sleep")
    time.sleep(60)




#icon
image_icon=PhotoImage(file="speaker logo.png")
root.iconphoto(False,image_icon)

# Top Frame
Top_frame = Frame(root,bg="#154c79", width=900, height=100)
Top_frame.place(x=0,y=0)


Label(Top_frame,text="Time pass", font="arial 36 bold", bg="#154c79", fg="white").place(x=350,y=20)


################
Top_frame = Frame(root,bg="#2e2e2d", width=250, height=500)
Top_frame.place(x=0,y=100)

btn=Button(root,text="YT", width=10, font="arial 14 bold", bg="#39c790",command=yt)
btn.place(x=400,y=160)
btn2=Button(root,text="CG", width=10, font="arial 14 bold", bg="#39c790",command=cg)
btn2.place(x=650,y=160)
btn3=Button(root,text="Sleep", width=10, font="arial 14 bold", bg="#39c790",command=sleep)
btn3.place(x=400,y=280)
btn4=Button(root,text="Exit", width=10, font="arial 14 bold", bg="#39c790",command=root.destroy)
btn4.pack()
btn4.place(x=650,y=280)


root.mainloop()
