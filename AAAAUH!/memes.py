import keyboard
import string
from threading import *
from playsound import playsound
from tkinter import *
import random
import os

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

def videos():
    import cv2
    import numpy as np
    import time
    from random import randint
    from ffpyplayer.player import MediaPlayer

    while True:

        rd1 = (randint(0,50))
        rd2 = (randint(0,50))

        time.sleep(2)

        if rd1 == rd2:

            print(f'RD1: {rd1} RD2: {rd2}\n')
            video_path="C:/Users/Guilherme/OneDrive/Área de Trabalho/ㅤ/Python/AAAAUH!/video.mp4"
            def PlayVideo(video_path):
                video=cv2.VideoCapture(video_path)
                player = MediaPlayer(video_path)
                while True:
                    grabbed, frame=video.read()
                    audio_frame, val = player.get_frame()
                    if not grabbed:
                        break
                    if cv2.waitKey(28) & 0xFF == ord("q"):
                        break
                    cv2.imshow("Video", frame)
                    if val != 'eof' and audio_frame is not None:
                        img, t = audio_frame
                video.release()
                cv2.destroyAllWindows()
            PlayVideo(video_path)

        else:
            print(f'RD1: {rd1} RD2: {rd2}\n')


root = Tk()
f
def esquerdo(event):
    print("Esquerdo em ({},{})".format(event.x, event.y))
    
def direito(event):
    print("Direito em ({},{})".format(event.x, event.y))

def scroll_meio(event):
    print("scroll_meio em ({},{})".format(event.x, event.y))

frame = Frame(root, width=300, height=300)
frame.bind("<Button-1>", esquerdo)
frame.bind("<Button-2>", scroll_meio)
frame.bind("<Button-3>", direito)
frame.pack()

root.mainloop()

videos()