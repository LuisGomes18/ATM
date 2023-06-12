'''
Json para poder extrair os dados dos ficheiros
'''
from json import loads

with open('Data/Dados_Login.json', 'r', encoding='utf-8') as dados_lg:
    conteudo = dados_lg.read()
    dados = loads(conteudo)

Numeros_das_Contas = [
    dados["Login_1"]["Numero_Conta"],
    dados["Login_2"]["Numero_Conta"],
    dados["Login_3"]["Numero_Conta"]]


def login():
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
            print('Acess Granted')
            break
        elif numero_conta in Numeros_das_Contas or password != password_usuario:
            print('Acess Denied')
