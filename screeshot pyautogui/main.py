from colorama import Fore, Back, Style
from playsound import playsound
from datetime import datetime
from time import strftime

import pyautogui
import keyboard
import os.path
import os

voltar = Style.RESET_ALL
verde = Fore.GREEN
vermelho = Fore.RED


data = datetime.today().strftime('%Y-%m-%d')
som = 1 # Padrão 1 
prints = 0 # Padrão 0
printar = 'z' # Padrão z
sair = 'b' # Padrão b
tcconfig = 'x' # Padrão x

if som == 1:
    somvt = f'{verde}On{voltar}'
else:
    somvt = f'{vermelho}Off{voltar}'


os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.RED + f'''
   3@              $2 
    2&            @3
     3!          @2
      2$        &2               
       3&@!$@&@@2                $ Seja bem-vindo ao Pyshot <3   
       2@@&@@&@!3                $ Programa feito por Gelado662
       2@3@@@@3@2                $ Pressione a telca "{printar}" para ScreenShot
       3@@3333@&2                $ Aperte ctrl + {sair} para sair
         2@&@@2                  $ Aperte ctrl + {tcconfig} para abir o menu de configurações
       2@&!@$$@@2
      3@@&@$@&@@@2
     2@!$@@&@!$&@$3
    2$2@@!&@!&@&@3@2
   3! 3@$@&@&@@&@2 @2
      2&@@@$$!&@@3
      3@@&@&@!@@@2
      2@@&@23$&@!3
      2@&@@32!@$&3
      3@&!@23&@@@2
      2&@$&32!@!&2
      2@@&@23!@&@3
       2322  3222

 ''')

while keyboard.is_pressed(f'ctrl+{sair}') == False:

    if keyboard.is_pressed(printar):

        if (os.path.exists(f'my_screenshot {data}.png')):

            while True:

                prints = prints + 1

                if (os.path.exists(f'my_screenshot {data} ({prints}).png')):

                    continue

                else:

                    printscreen = pyautogui.screenshot()
                    printscreen.save(f'my_screenshot {data} ({prints}).png')
                    print(Fore.GREEN + f'[!] Salvo my_screenshot {data} ({prints}).png')

                    if som == 1:

                        playsound('C:/python_arquivos/screenshot.mp3')

                        prints = prints = 0

                        break

                    else:

                        prints = prints = 0

                        break

        else:

            printscreen = pyautogui.screenshot()
            printscreen.save(f'my_screenshot {data}.png')
            print(Fore.GREEN + f'[!] Salvo my_screenshot {data}.png')
            if som == 1:
                playsound('C:/python_arquivos/screenshot.mp3')
            else:
                break

    elif keyboard.is_pressed(f'ctrl+{tcconfig}'):

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''{voltar}Configurações

[???]

[{somvt}] Som

[Teclas]

[{printar}] Tecla de printscreen
[ctrl + {sair}] Tecla de sair/voltar
[ctrl + {tcconfig}] Tecla de configurações

Aperte ctrl + {sair} para voltar''')

        op = input('>> ')