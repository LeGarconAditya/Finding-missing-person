from tkinter import *
import os
from PIL import Image,ImageTk


win=Tk()
win.title("FACE RECOGNITION USING CNN")
win.configure(bg="#000000")
win.geometry("1500x750")
img=Image.open("aa.jpg")
img=img.resize((1500,750))
bg=ImageTk.PhotoImage(img)

lbl=Label(win,image=bg)
lbl.place(x=0,y=0)

def run_file():
    command = 'python.exe .\\main.py .\\20170512-110547\\20170512-110547.pb .\\20170512-110547\\ids\\'
    os.system(command)
label=Label(win,text="FINDING MISSING PERSON",bg="black",fg="white",font=("times",25,"bold"))
label.place(x=700,y=25)

label=Label(win,text=" Click below button to run the project",bg="black",fg="white",font=("times",25,"bold"))
label.place(x=700,y=150)

label=Button(win,text="Start",bg="black",fg="white",font=("times",25,"bold"),command=run_file)
label.place(x=900,y=340)




win.mainloop()

