import pyautogui
import time
import cv2
import keyboard

img = cv2.imread(r"C:\Users\Guilherme\Desktop\testes python\Trabalho de artes\arquitetura.jpg")



while keyboard.is_pressed("q") == False:
    try:
        acc_co = \
            pyautogui.locateOnScreen(
                img,
                confidence=.7
                )      
        acc_co = pyautogui.center(acc_co)
        x, y = acc_co.x, acc_co.y
        pyautogui.click(x, y)
    except:
        print("Não encontrado")