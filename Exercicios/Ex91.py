from random import randrange

# Estética
hist = []
user = {}
cont = 0
print('-=' * 30)
print(f'{"GERADOR DE DADOS DE RPG":^60}')
print('-=' * 30)

# Entrada
while True:
    quant = input("Digite quantos jogadores rolarão o dado: ")
    if quant[0].isnumeric():
        quant = int(quant)
        break
    else:
        print('-=' * 30)
        print(f'\033[1:31m{"DIGITE UM NÚMERO VÁLIDO!":^60}\033[m')
        print('-=' * 30)
print('-' * 30)

# Processamento
for i in range(1, quant + 1):
    title = '''[ 1 ] Dado d4
[ 2 ] Dado d6
[ 3 ] Dado d8
[ 4 ] Dado d10
[ 5 ] Dado d12
[ 6 ] Dado d20
[ 7 ] Dado d100
[ 8 ] Dado customizável'''
    user['Jogador'] = input('Nome do jogador: ').capitalize().strip()
    print('-' * 30)
    while True:
        print(title)
        user['Opcao'] = input('Escolha: ')
        if user['Opcao'] not in "12345678":
            print('-=' * 30)
            print(f'\033[1:31m{"SELECIONE UMA OPÇÃO VÁLIDA!":^60}\033[m')
            print('-=' * 30)
        else:
            break
    print('-=' * 30)

    match user['Opcao']:
        case '1':
            user['Tipo'] = "D4"
            user['Dados'] = randrange(1, 5)

        case '2':
            user['Tipo'] = "D6"
            user['Dados'] = randrange(1, 7)

        case '3':
            user['Tipo'] = "D8"
            user['Dados'] = randrange(1, 9)

        case '4':
            user['Tipo'] = "D10"
            user['Dados'] = randrange(1, 11)

        case '5':
            user['Tipo'] = "D12"
            user['Dados'] = randrange(1, 13)

        case '6':
            user['Tipo'] = "D20"
            user['Dados'] = randrange(1, 21)

        case '7':
            user['Tipo'] = "D100"
            user['Dados'] = randrange(1, 101)

        case '8':
            while True:
                quantL = input("Digite quantos números o dado vai ter: ")
                if quantL.find('.') != -1:
                    print('-=' * 30)
                    print(f'\033[1:31m{"DIGITE UM NÚMERO INTEIRO!":^60}\033[m')
                    print('-=' * 30)
                    cont += 1
                    if cont == 2:
                        while True:
                            arrendondar = input('\033[31mDeseja arredondar o número? \033[m')
                            print('-=' * 30)
                            if arrendondar[0] not in "SsNn":
                                print('-=' * 30)
                                print(f'\033[1:31m{"DIGITE UMA RESPOSTA VÁLIDA":^60}\033[m')
                                print('-=' * 30)
                            else:
                                if arrendondar[0] in "Ss":
                                    quantL = float(quantL)
                                    quantL = round(quantL)
                                    quantL = int(quantL)
                                    break

                                else:
                                    print('-=' * 30)
                                    print(f'\033[1:31m{"DIGITE UM NÚMERO INTEIRO!":^60}\033[m')
                                    print('-=' * 30)
                                    break

                        if type(quantL) == int:
                            break

                else:
                    quantL = int(quantL)
                    break

            while True:
                zero_um = input("O zero é uma possibilidade de resultado? [S/N] ")
                if zero_um.isalpha():
                    if zero_um[0] in "Ss":
                        zero_um = 0
                        break
                    elif zero_um[0] in "Nn":
                        zero_um = 1
                        break
                else:
                    print('-=' * 30)
                    print(f'\033[1:31m{"DIGITE UMA OPÇÃO VÁLIDA!":^60}\033[m')
                    print('-=' * 30)

            print('-=' * 30)

            quantL = str(quantL)
            user['Tipo'] = "D" + quantL
            quantL = int(quantL)
            user['Dados'] = randrange(zero_um, quantL)

        case _:
            pass

    del user['Opcao']
    hist.append(user.copy())
    cont = 0

# Ordenando a lista com base no resultado dos dados
hist = sorted(hist, key=lambda x: x['Dados'], reverse=True)

# Saída
print('-' * 59)
title = "HISTÓRICO"
print(f'{title:^59}')
print('-' * 59)

print(f"{'Jogador':^20} | {'Tipo do Dado':^20} | {'Valor':^10}")
print(f'{"-" * 20:^20} | {"-" * 20:^20} | {"-" * 13:^10}')
for i in hist:
    print(f"{i['Jogador']:^20} | {i['Tipo']:^20} | {i['Dados']:^10}")

print('-=' * 30)
print("\033[31mSaindo...\033[m")
print("\033[35mCódigo feito por Goi 2ºDS\033[m")
