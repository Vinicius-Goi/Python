from random import randrange
continuar = ""
hist = list()
user = dict()
title = 'GERADOR DE DADOS'
print('-='*15)
print(f'{title:^30}')
print('-='*15)
quant = int(input("Digite quantos jogadores rolarão o dado: "))
print('-='*15)
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
    user['Jogador'] = str(input('Nome do jogador: ')).capitalize()
    user['Opcao'] = str(input('Escolha: '))
    print('-=' * 30)
    while user['Opcao'] not in '1234567':
        print('\033[1:31mSELECIONE UMA OPÇÃO VALIDA!\033[m')
        print('-=' * 30)
        print(title)
        user['Opcao'] = str(input('Escolha: '))
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


print('-' * 59)
title = "HISTÓRICO"
print(f'{title:^59}')
print('-' * 59)

print(f"{'Jogador':^20} | {'Tipo do Dado':^20} | {'Valor':^10}")
for i in hist:
    print(f"{i['Jogador']:^20} | {i['Tipo']:^20} | {i['Dados']:^10}")

print("\n\033[31mSaindo...\033[m")
print("\033[35mCódigo feito por Goi 2ºDS\033[m")