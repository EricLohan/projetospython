from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario',size=(10,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(10,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]

]
#Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'erick' and valores['senha'] == '0800909009':
            print('Bem-Vindo a sua primeira Tela')