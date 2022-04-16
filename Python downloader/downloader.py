from matplotlib.pyplot import title
from pytube import YouTube, streams
from pytube.cli import on_progress
import colorama 

url =input(str('Url para download: '))

fuchsia = '\033[38;2;255;00;255m'   #  color as hex #FF00FF
reset_color = '\033[39m'


def download_youtube():

    video = YouTube(url, on_progress_callback=on_progress)

    print(f'\n' + fuchsia + 'Downloading: ', video.title, '~ viewed', video.views, 
    'times.')

    stream = video.streams.get_highest_resolution()

    video.streams.first().download('.\\downloads\\')

    print(f'\nFinished downloading:  {video.title}' + reset_color)

download_youtube()