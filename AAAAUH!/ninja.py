from pynput.keyboard import Key, Controller
import pyautogui
import keyboard
import time
import os

def ninja():

    while keyboard.is_pressed("x") == False:

        keyboard.press_and_release('')
        keyboard.press_and_release('LMENU')
        posit = pyautogui.position()
        pyautogui.rightClick(posit)
        time.sleep(0.5)
        continue

while True:

    if keyboard.is_pressed("z"):

        ninja()

    elif keyboard.is_pressed("p"):
        break
