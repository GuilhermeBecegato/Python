from matplotlib.pyplot import title
from pytube import YouTube, streams
from pytube.cli import on_progress

import moviepy.editor as mp
import os

url =input('URL: ')
user = os.getenv('USERNAME')

link = url

if 'www.youtube.com/' in url.lower():

    video = YouTube(link, on_progress_callback=on_progress).streams.get_audio_only()
            
    print(f'\nDownloading: {video.title}')

    video.download(rf'C:\Users\{user}\Desktop')

    title = str(video.title)

    clip = mp.AudioFileClip(rf'C:\Users\{user}\Desktop\{title}.mp4')
    clip.write_audiofile(rf'C:\Users\{user}\Desktop\{title}.mp3')

    os.remove(rf'C:\Users\{user}\Desktop\{title}.mp4')

    print(f'\nFinished downloading:  {title}')