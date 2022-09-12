from gtts import gTTS
import os
from tkinter import *
root=Tk()
canvas=Canvas(root,width=400,height=300)
canvas.pack()

def text():
    text=entry.get()
    output=gTTS(text=text,lang='en',slow=False)
    output.save('output3.mp3')
    os.system('start output3.mp3')
entry=Entry(root)
canvas.create_window(200,180,window=entry)
bt=Button(text='start',command=text)
canvas.create_window(200,230,window=bt)

root.mainloop()
