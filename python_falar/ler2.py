import gtts
from playsound import playsound
import os
import time

caminho = 'C:/Users/Guilherme/Desktop/testes_python/python_falar/arquivo.mp3'

while True:

    text =input('>> ')

    arquivo = open("frases.txt", "w")
    arquivo.write(text)


    print('Lendo arquivo...')
    with open('frases.txt', 'r') as arquivo:
        for linha in arquivo:
            frase = gtts.gTTS(linha, lang='pt-br')
        print('Gerando arquivo...')
        frase.save('arquivo.mp3')
        time.sleep(2)
        print('Abrindo arquivo...')
        playsound(caminho)
        print('Arquivo lido\nExcluindo arquivo criado')
        os.remove('arquivo.mp3')
