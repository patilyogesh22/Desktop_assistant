# gui of zara
from tkinter import *  #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow 
import time
import pygame  #pip install pygame(piche ka music esse chakta hai )
from pygame import mixer #The mixer module allows you to load, play, and control audio files (like .mp3 or .wav), making it useful for applications that need sound effects or background music.
mixer.init()

root = Tk()
root.geometry("1900x1000")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("giphy.webp")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load ("IntroSound.wav")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1900,1000))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.08)
    root.destroy()

play_gif()
root.mainloop()

