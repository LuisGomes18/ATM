"""
Instala o modulo paras gerar numero aleatorio
Instala o modulo para verificar se ficheiro existe e apagalo caso necessario
Instala o modulo pqra fazer qrcodes
"""
from random import randint
from os import path
from os import remove
from qrcode import make  # pylint: disable=E0401

DEBUG = 0

def metodo_dois_factores():
    '''
    Função de dois factores
    '''
    while True:
        numero_sorteado = randint(100000, 999999)
        if path.exists("Dois_Factores.png"):
            remove("Dois_Factores.png")
        else:
            pass

        img = make(f'{numero_sorteado}')
        type(img)
        img.save("Dois_Factores.png")

        numero_usuario = int(input('\n\nInsira o numero do 2 factores: '))
        if numero_sorteado == numero_usuario:
            print('\nAcesso Granted')
            break
        elif numero_sorteado != numero_usuario:
            print('\nAcess Denied')

if DEBUG == 0:
    pass
else:
    metodo_dois_factores()
