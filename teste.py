import PySimpleGUI as sg

sg.theme('DarkBlue5')

def front():
    flayout = [
        [sg.Text('Seja Bem-Vindo')],
        [sg.Button('Cadastro')],
        [sg.Button('Login')],
        [sg.Button('Sair')]
    ]

    window = sg.Window('projeto_cadastro', flayout, element_justification='center')
    button, values = window.read()

    if button == 'Cadastro':
        window.close()
        cadastrar()

    if button == 'Login':
        window.close()
        fazer_login()

    if button == 'Sair':
        window.close()

def cadastrar():
    layout = [
        [sg.Text('Insira seu email para cadastro:'), sg.InputText('', key='-LOGIN-')],
        [sg.Text('Insira sua senha para cadastro:'), sg.InputText('', key='-PASSWORD-')],
        [sg.Text('')],
        [sg.Button('Cadastrar'), sg.Button('Voltar')]
    ]

    window = sg.Window('Tela de Cadastro', layout)
    while True:
        button, event, values = window.read()

        if button == 'Voltar' or button == sg.WIN_CLOSED:
            window.close()
            front()

        if event == 'Cadastrar':
            login = values['-LOGIN-']
            senha = values['-PASSWORD-']
            # Aqui você pode adicionar a lógica de cadastro com os dados fornecidos
            # por exemplo, armazená-los em algum lugar ou realizar validações
            # Lembre-se de adicionar essa lógica aqui

    window.close()

def fazer_login():
    layout = [
        [sg.Text('Insira seu email para cadastro:'), sg.InputText('', key='-LOGIN-')],
        [sg.Text('Insira sua senha para cadastro:'), sg.InputText('', key='-PASSWORD-')],
        [sg.Text('')],
        [sg.Button('Cadastrar'), sg.Button('Voltar')]
    ]

    window = sg.Window('Tela de Login', layout)
    while True:
        button, event, values = window.read()

        if button == 'Voltar' or button == sg.WIN_CLOSED:
            window.close()
            front()

        # Aqui você pode adicionar a lógica de login

front()
