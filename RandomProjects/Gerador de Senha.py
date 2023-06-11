import random

print('Bem Vindo ao Gerador de Senhas')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

numeros = int(input('Digite a \033[1mQUANTIDADE DE SENHAS\033[m que deseja gerar: '))

comprimento = int(input('Digite a \033[1mQUANTIDADE DE CARACTERES\033[m que deseja ter na senha: '))

print('''
Aqui está suas senhas:''')

for snh in range(numeros):
    senhas = ''
    for c in range(comprimento):
        senhas += random.choice(caracteres)
    print(senhas)
