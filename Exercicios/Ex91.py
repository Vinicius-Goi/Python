from random import randrange
    
#Estética
hist = list()
user = dict()
print('-='*15)
print(f'{"GERADOR DE DADOS DE RPG":^30}')
print('-='*15)


#Entrada
while True:
    quant = input("Digite quantos jogadores rolarão o dado: ")
    if quant[0].isnumeric():
        quant = int(quant)
        break
    else:
        print('-'*30)
        print(f'\033[1:31m{"DIGITE UM NÚMERO VÁLIDO!":^30}\033[m')
        print('-' * 30)
print('-='*15)


#Processamento
for i in range(1, quant+1):
    title = '''[ 1 ] Dado d4
[ 2 ] Dado d6
[ 3 ] Dado d8
[ 4 ] Dado d10
[ 5 ] Dado d12
[ 6 ] Dado d20
[ 7 ] Dado d100
'''
    print(title)
    user['Jogador'] = str(input('Nome do jogador: ')).capitalize().strip()

    while True:
        user['Opcao'] = str(input('Escolha: '))
        if user['Opcao'] not in "1234567":
            print('\033[1:31mSELECIONE UMA OPÇÃO VÁLIDA!\033[m')
            print('-=' * 30)
        else:
            break
    print('-=' * 30)

    if user['Opcao'] == '1':
        cpu = randrange(1, 5)
        user['Tipo'] = "D4"
        user['Dados'] = cpu

    elif user['Opcao'] == '2':
        cpu = randrange(1, 7)
        user['Tipo'] = "D6"
        user['Dados'] = cpu

    elif user['Opcao'] == '3':
        user['Tipo'] = "D8"
        cpu = randrange(1, 9)
        user['Dados'] = cpu

    elif user['Opcao'] == '4':
        user['Tipo'] = "D10"
        cpu = randrange(1, 11)
        user['Dados'] = cpu

    elif user['Opcao'] == '5':
        user['Tipo'] = "D12"
        cpu = randrange(1, 13)
        user['Dados'] = cpu

    elif user['Opcao'] == '6':
        user['Tipo'] = "D20"
        cpu = randrange(1, 21)
        user['Dados'] = cpu

    else:
        cpu = randrange(1, 101)
        user['Tipo'] = "D100"
        user['Dados'] = cpu

    del user['Opcao']
    hist.append(user.copy())


#Saída
print('-' * 59)
title = "HISTÓRICO"
print(f'{title:^59}')
print('-' * 59)

print(f"{'Jogador':^20} | {'Tipo do Dado':^20} | {'Valor':^10}")
for i in hist:
    print(f"{i['Jogador']:^20} | {i['Tipo']:^20} | {i['Dados']:^10}")

print("\n\033[31mSaindo...\033[m")
print("\033[35mCódigo feito por Goi 2ºDS\033[m")