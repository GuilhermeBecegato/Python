import cv2
import numpy as np
import time
from random import randint

#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer

while True:

    rd1 = (randint(0,10))
    rd2 = (randint(0,10))

    time.sleep(20)

    if rd1 == rd2:

        print(f'RD1: {rd1} RD2: {rd2}')
        video_path="C:/Users/Guilherme/OneDrive/Área de Trabalho/ㅤ/Python/AAAAUH!/video.mp4"
        def PlayVideo(video_path):
            video=cv2.VideoCapture(video_path)
            player = MediaPlayer(video_path)
            while True:
                grabbed, frame=video.read()
                audio_frame, val = player.get_frame()
                if not grabbed:
                    print("End of video")
                    break
                if cv2.waitKey(28) & 0xFF == ord("q"):
                    break
                cv2.imshow("Video", frame)
                if val != 'eof' and audio_frame is not None:
                    #audio
                    img, t = audio_frame
            video.release()
            cv2.destroyAllWindows()
        PlayVideo(video_path)
    
    else:
        print(f'RD1: {rd1} RD2: {rd2}')
