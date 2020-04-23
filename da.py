from tkinter import *
import tkinter as tk
import speech_recognition as sr
from io import open
import time, sys
from pygame import mixer
mixer.init()

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
    except:
        print("Im sorry")
    if(format(text)=="hello"):
        sound = mixer.Sound('hola.wav')
        sound.play()
        time.sleep(1)
    elif(format(text=="how are you")):
        sound = mixer.Sound('hola.wav')
        sound.play()
        time.sleep(1)
    elif(format(text=="what do you do")):
        sound = mixer.Sound('hola.wav')
        sound.play()
        time.sleep(1)

