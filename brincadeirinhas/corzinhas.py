import keyboard
import psutil

ram = psutil.virtual_memory()._asdict()

cpu = psutil.cpu_percent()

vrs =input('Começar? y/n >> ')

def main():

    while keyboard.is_pressed('z') == False:

        print(ram + ram + ram + ram)
        print(cpu + cpu + cpu + cpu)

main()