import keyboard
import string
from threading import *

"""

Optional code(extra keys):

keys.append("space_bar")
keys.append("backspace")
keys.append("shift")
keys.append("esc")

"""

# Atribuo a lista de caracteres ascii para a variavel keys(não encontrei lista com todas as teclas)
teclas = list(string.ascii_lowercase)
teclas2 = list(string.append("space_bar"))


def listen(tecla, teclas2):
    while True:
        keyboard.wait(tecla, teclas2)
        print("- Tecla pressionada: ",tecla)

threads = [Thread(target=listen, kwargs={"tecla":tecla}) for tecla in teclas]

for thread in threads:
    thread.start()