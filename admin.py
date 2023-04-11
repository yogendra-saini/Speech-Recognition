import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Debuggers")
root.geometry("1000x550+200+200")
root.resizable(False,False)
root.configure(bg="#19A7CE")



#icon
image_icon=PhotoImage(file="speaker logo.png")
root.iconphoto(False,image_icon)

# Top Frame
Top_frame = Frame(root,bg="#143C94", width=1000, height=100)
Top_frame.place(x=0,y=0)


Label(Top_frame,text="Admin Panel", font="arial 36 bold", bg="#143C94", fg="white").place(x=300,y=20)


################
Top_frame = Frame(root,bg="#000000", width=250, height=500)
Top_frame.place(x=0,y=100)


Label(root,text="Education",font="arial 24 bold", bg="#19A7CE", fg="Black").place(x=350,y=190)
btn=Button(root,text="Open", width=10, font="arial 14 bold", bg="#19A7CE")
btn.place(x=600,y=190)
Label(root,text="Medical",font="arial 24 bold", bg="#19A7CE", fg="black").place(x=350,y=270)
btn=Button(root,text="Open", width=10, font="arial 14 bold", bg="#19A7CE")
btn.place(x=600,y=270)
Label(root,text="Translator",font="arial 24 bold", bg="#19A7CE", fg="black").place(x=350,y=350)
btn=Button(root,text="Open", width=10, font="arial 14 bold", bg="#19A7CE")
btn.place(x=600,y=350)






root.mainloop()
