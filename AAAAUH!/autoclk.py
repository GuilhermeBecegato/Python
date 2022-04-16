import pyautogui
import keyboard

#def autoclick():

    #while keyboard.is_pressed("z") == False:
        #posit = pyautogui.position()
        #pyautogui.doubleClick(posit)

def rightclick():
    while keyboard.is_pressed("x") == False:
        posit = pyautogui.position()
        pyautogui.rightClick(posit)

while True:
    #if keyboard.is_pressed("'"):
        #autoclick()
        
    if keyboard.is_pressed('"'):
        rightclick()

    else:
        continue