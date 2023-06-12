"""
Instala o modulo paras gerar numero aleatorio
Instala o modulo para verificar se ficheiro existe e apagalo caso necessario
Instala o modulo pqra fazer qrcodes
"""
import random
import os
import qrcode  # pylint: disable=E0401


def dois_factores():
    '''
    Função de dois factores
    '''
    numero_sorteado = random.randint(100000, 999999)
    if os.path.exists("Dois_Factores.png"):
        os.remove("Dois_Factores.png")
        print("Arquivo Dois_Factores.png removido com sucesso.")
    else:
        print("O arquivo Dois_Factores.png não existe.")

    img = qrcode.make(f'{numero_sorteado}')
    type(img)
    img.save("Dois_Factores.png")

    numero_usuario = int(input('Insira o numero do 2 factores: '))
    if numero_sorteado == numero_usuario:
        print('Acesso granted')
