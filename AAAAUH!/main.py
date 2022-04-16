import keyboard
import string
from threading import *
from playsound import playsound
import random
import os

import cv2
import pafy

url = 'https://www.youtube.com/watch?v=ZVbhr-mu-_U&list=PL4ph19QOeFMBUVIqGCGxG2AaI9uaHAwrn&index=43'
videoPafy = pafy.new(url)
best = videoPafy.getbest(preftype='mp4')

cap = cv2.VideoCapture(best.url)


teclas = list(string.ascii_lowercase)

som1 = 'C:/python_arquivos/som1.mp3'
som2 = 'C:/python_arquivos/som2.mp3'
som3 = 'C:/python_arquivos/som3.mp3'
som4 = 'C:/python_arquivos/som4.mp3'
som5 = 'C:/python_arquivos/som5.mp3'
som6 = 'C:/python_arquivos/som6.mp3'
som7 = 'C:/python_arquivos/som7.mp3'
som8 = 'C:/python_arquivos/som8.mp3'
som9 = 'C:/python_arquivos/som9.mp3'
som10 = 'C:/python_arquivos/som10.mp3'
som11 = 'C:/python_arquivos/sound1.mp3'
som12 = 'C:/python_arquivos/sound2.mp3'
som13 = 'C:/python_arquivos/sound3.mp3'
som14 = 'C:/python_arquivos/som14.mp3'
som15 = 'C:/python_arquivos/som15.mp3'
som16 = 'C:/python_arquivos/som16.mp3'
som17 = 'C:/python_arquivos/som17.mp3'
som18 = 'C:/python_arquivos/som18.mp3'
som19 = 'C:/python_arquivos/som19.mp3'
som20 = 'C:/python_arquivos/som20.mp3'
som21 = 'C:/python_arquivos/som21.mp3'
som22 = 'C:/python_arquivos/som22.mp3'
som23 = 'C:/python_arquivos/som23.mp3'
som24 = 'C:/python_arquivos/som24.mp3'
som25 = 'C:/python_arquivos/som25.mp3'
som26 = 'C:/python_arquivos/som26.mp3'
som27 = 'C:/python_arquivos/som27.mp3'

memes = [som1, som2, som3, som4, som5, som6, som7, som8, som9, som10, som11, som12, som13, som14, som15, som16, som17, som18, som19, som20, som21, som22, som23, som24, som25, som26, som27]

os.system('cls' if os.name == 'nt' else 'clear')

def teclass(tecla):

    while True:

        keyboard.wait(tecla)
        alt = random.choice(memes)
        print(F'Você pressionou:  {tecla}\nTocou:  {alt}\n')
        playsound(alt)
        

threads = [Thread(target=teclass, kwargs={"tecla":tecla}) for tecla in teclas]

for thread in threads:
    thread.start()