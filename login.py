'''
Json para poder extrair os dados dos ficheiros
'''
from json import loads
from pathlib import Path
from dois_factores import metodo_dois_factores

with open('Data/Dados_Login.json', 'r', encoding='utf-8') as dados_lg:
    conteudo = dados_lg.read()
    dados = loads(conteudo)

Numeros_das_Contas = [
    dados["Login_1"]["Numero_Conta"],
    dados["Login_2"]["Numero_Conta"],
    dados["Login_3"]["Numero_Conta"]]

DEBUG = 0
CAMINHO_DO_FICHEIRO = "/workspaces/ATM/Dois_Factores.png"
caminho_ficheiro = Path(CAMINHO_DO_FICHEIRO)

def logins():
    '''
    Login
    '''
    numero_conta = int(input('Numero da conta: '))
    password = int(input('Password: '))
    while True:
        if numero_conta == dados["Login_1"]["Numero_Conta"]:
            password_usuario = dados["Login_1"]["Password"]
        elif numero_conta == dados["Login_2"]["Numero_Conta"]:
            password_usuario = dados["Login_1"]["Password"]
        elif numero_conta == dados["Login_3"]["Numero_Conta"]:
            password_usuario = dados["Login_1"]["Password"]
        if numero_conta in Numeros_das_Contas and password == password_usuario:
            metodo_dois_factores()
            break
        elif numero_conta in Numeros_das_Contas or password != password_usuario:
            print('Acess Denied')

    if caminho_ficheiro.exists():
        caminho_ficheiro.unlink()
    else:
        pass

if DEBUG == 0:
    pass
else:
    logins()
