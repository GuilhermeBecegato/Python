import gtts
from playsound import playsound

text =input('')

print('Lendo arquivo...')
with open('frases.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        print('Gerando arquivo...')
        frase.save('arquivo.mp3')
        print('Abrindo arquivo...')
        playsound('arquivo.mp3')
        print('Arquivo lido')