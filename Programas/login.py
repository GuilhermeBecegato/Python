from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkPurple2')

#layout

layout = [
    [sg.Text('Usuario'),sg.Input(key='user', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar login')],
    [sg.Button('Entrar')]
]

#janela

janela = sg.Window('Tela de login', layout)

#ler eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['user'] == 'guilherme' and valores['senha'] == '1234':
            print("oi")