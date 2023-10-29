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
    button,  values = window.read()

    if button == 'Cadastro':
        window.close()

    if button == 'Login':
        window.close()

    if button == 'Sair':
        window.exit()

layout = [
    [sg.Text('Insira seu email para cadastro:', sg.InputText(''), key='-LOGIN-')],
    [sg.Text('Insira sua senha para cadastro:', sg.InputText(''), key='-PASSWORD-')],
    [sg.Text('')],
    [sg.Button('Cadastrar'), sg.Button('Voltar')]

]

front()

window = sg.Window('Tela de Cadastro', layout)

button, values = window.read()








#while True:
 #   eventos, valores = janela.read()
  #  if eventos == sg.WINDOW_CLOSED:
   #     break
    #if eventos == 'Entrar':
     #   if valores['usuario'] == 'erick' and valores['senha'] == '0800909009':
      #      print('bemvindo')