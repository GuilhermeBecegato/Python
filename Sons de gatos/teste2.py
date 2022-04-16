import keyboard
import string
from threading import *
from playsound import playsound
import random

teclas = list(string.ascii_lowercase)

gato1 = 'C:/python_arquivos/gato1.mp3'
gato2 = 'C:/python_arquivos/gato2.mp3'
gato3 = 'C:/python_arquivos/gato3.mp3'
gato4 = 'C:/python_arquivos/gato4.mp3'
gato5 = 'C:/python_arquivos/gato5.mp3'
gato6 = 'C:/python_arquivos/gato6.mp3'
gato7 = 'C:/python_arquivos/gato7.mp3'

miado = [gato1, gato2, gato3, gato4, gato5, gato6, gato7]



def teclass(tecla):

    while True:

        keyboard.wait(tecla)
        miadoesc = random.choice(miado)
        print(F'Você pressionou:  {tecla}\nTocou:  {miadoesc}\n')
        playsound(miadoesc)
        

threads = [Thread(target=teclass, kwargs={"tecla":tecla}) for tecla in teclas]

for thread in threads:
    thread.start()