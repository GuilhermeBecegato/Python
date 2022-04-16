import pyautogui
import pyautogui as py
import keyboard
import time
import cv2

img = cv2.imread(r"C:\Users\Guilherme\Desktop\testes python\pyautogui\file.jpg") 

# 611 618
# (38, 35, 52)

while keyboard.is_pressed("q") == False:
    s = py.locateOnScreen(img,confidence=0.9)
    print(s)