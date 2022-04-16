from colorama import Fore, Back, Style
from playsound import playsound

import random
import os

tracks = ['', '', '']

gato1 = 'C:/python_arquivos/gato1.mp3'
gato2 = 'C:/python_arquivos/gato2.mp3'
gato3 = 'C:/python_arquivos/gato3.mp3'
gato4 = 'C:/python_arquivos/gato4.mp3'
gato5 = 'C:/python_arquivos/gato5.mp3'
gato6 = 'C:/python_arquivos/gato6.mp3'
gato7 = 'C:/python_arquivos/gato7.mp3'

miado = [gato1, gato2, gato3, gato4, gato5, gato6, gato7]

os.system('cls' if os.name == 'nt' else 'clear')

while True:

    musica = random.choice(miado)

    print(f'Tocando agora: {musica}\n')

    playsound(musica)