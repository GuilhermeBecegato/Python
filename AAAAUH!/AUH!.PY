import keyboard
import string
from threading import *
from playsound import playsound
import random

teclas = list(string.ascii_lowercase)

som_1 = 'C:/python_arquivos/sound1.mp3'
som_2 = 'C:/python_arquivos/sound2.mp3'
som_3 = 'C:/python_arquivos/sound3.mp3'

auuh = [som_1, som_2, som_3]

def teclass(tecla):

    while True:

        keyboard.wait(tecla)
        auht = random.choice(auuh)
        print(F'Você pressionou:  {tecla}\nTocou:  {auht}\n')
        playsound(auht)
        

threads = [Thread(target=teclass, kwargs={"tecla":tecla}) for tecla in teclas]

for thread in threads:
    thread.start()