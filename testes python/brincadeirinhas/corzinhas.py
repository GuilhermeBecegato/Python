import keyboard
import psutil

ram = psutil.virtual_memory()._asdict()

cpu = psutil.cpu_percent()

disk = psutil.disk_usage('/')

sensors = psutil.sensors_temperatures()

vrs =input('Começar? y/n >> ')

def main():

    while keyboard.is_pressed('z') == False:

        print(ram)
        print(cpu)

main()