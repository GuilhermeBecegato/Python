import PySimpleGUI as sg
import os
import requests

class clima:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Cidade', size=(5,1)), sg.Input(key='cidade', size=(25,1))],
            [sg.Output(size=(50, 20))],
            [sg.Button('Pesquisar cidade')]
            
        ]

        self.janela = sg.Window('Previsão do tempo', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Pesquisar cidade':
                nova_cidade = self.gerar_dados(valores)
                print(nova_cidade)

    def gerar_dados(self, valores):
        API_KEY = 'f90946e0798b36114441a2b458d4bfcd'
        cidade = valores['cidade']
        link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}'
        request = requests.get(link)    
        request.dic = request.json()
        return request.json()

clt = clima()
clt.Iniciar()