from pynput.keyboard import Key, Controller
import pyautogui
import keyboard
import time

teclado = Controller()

while keyboard.is_pressed('z') == False:

    posit = pyautogui.position()
    pyautogui.rightClick(posit)
    teclado.press('s')
    teclado.press('d')
    time.sleep(0.5)
    teclado.press(Key.alt)
    teclado.release('s')
    teclado.release('d')
    teclado.release(Key.alt)
    posit = pyautogui.position()
    pyautogui.rightClick(posit)