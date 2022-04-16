from matplotlib.pyplot import title
from pytube import YouTube, streams
from pytube.cli import on_progress

import moviepy.editor as mp
import PySimpleGUI as sg
import requests
import time
import os

user = os.getenv('USERNAME')


class downloader:

    def __init__(self):

        sg.theme('DarkGrey13')

        layout = [

            [sg.Text(f'Seja bem-vindo {user}!', size=(50,1))],
            [sg.Text('URL ', size=(5,1)), sg.Input(key='url', size=(50,1))],
            [sg.Output(size=(115, 20))],
            [sg.Button('Baixar mp4', size=(50,2))],
            [sg.Button('Baixar mp3', size=(50,2)), sg.Button('Sair', size=(50,2))],

        ]

        self.janela = sg.Window('Youtube Downloader', layout)

    def Iniciar(self):

        while True:

            evento, valores = self.janela.read()

            if evento == sg.WINDOW_CLOSED or evento == 'Sair':

                print('\nAté logo...')

                time.sleep(1)

                break

            if evento == 'Baixar mp4':

                baixarvideo = self.download_youtube(valores)

            elif evento == 'Baixar mp3':

                baixarvideomp3 = self.download_youtubemp3(valores)

    def download_youtube(self, valores):

        if 'www.youtube.com/' in valores['url'].lower():

            link = valores['url']

            video = YouTube(link, on_progress_callback=on_progress)

            print(f'\nDownloading: {video.title}')

            stream = video.streams.get_highest_resolution()

            title = str(video.title)

            video.streams.first().download(rf'C:\Users\{user}\Desktop\mp4\{title}.mp4')

            print(f'\nFinished downloading:  {video.title}')

        else:

            print('\nUse um link do YouTube valido!')

    def download_youtubemp3(self, valores):

        if 'www.youtube.com/' in valores['url'].lower():

            link = valores['url']

            video = YouTube(link, on_progress_callback=on_progress).streams.get_audio_only()
            
            print(f'\nDownloading: {video.title}')

            video.download(rf'C:\Users\{user}\Desktop')

            title = str(video.title)

            clip = mp.AudioFileClip(rf'C:\Users\{user}\Desktop\{title}.mp4') # Problema na hora de converter 27/03

            clip.write_audiofile(rf'C:\Users\{user}\Desktop\{title}.mp3') # Muitas informações no console 27/03

            os.remove(rf'C:\Users\{user}\Desktop\{title}.mp4')

            print(f'\nFinished downloading:  {title}')

        else:
            
            print('\nUse um link do YouTube valido!')


clt = downloader()
clt.Iniciar()