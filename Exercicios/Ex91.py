from random import randrange
for nome in range(1, 5):
    user = dict()
    jogadores = list()
    title = 'GERADOR DE DADOS'
    print('-='*15)
    print(f'{title:^30}')
    print('-='*15)
    title = '''[ 1 ] Dado d4
[ 2 ] Dado d6
[ 3 ] Dado d8
[ 4 ] Dado d10
[ 5 ] Dado d12
[ 6 ] Dado d20
    '''
    print(title)
    user['Jogador'] = str(input('Nome do jogador: '))
    user['Opcao'] = str(input('Escolha: '))
    print('-='*30)
    while user['Opcao'] not in '123456':
        print('SELECIONE UMA OPÇÃO VALIDA!')
        print('-=' * 30)
        print(title)
        user = str(input('Escolha: '))
        print('-='*30)

    if user['Opcao'] == '1':
        cpu = randrange(1, 5)
        user['Dados'] = cpu

    elif user['Opcao'] == '2':
        cpu = randrange(1, 7)
        user['Dados'] = cpu

    elif user['Opcao'] == '3':
        cpu = randrange(1, 9)
        user['Dados'] = cpu

    elif user['Opcao'] == '4':
        cpu = randrange(1, 11)
        user['Dados'] = cpu

    elif user['Opcao'] == '5':
        cpu = randrange(1, 13)
        user['Dados'] = cpu

    else:
        cpu = randrange(1, 21)
        user['Dados'] = cpu

    del user['Opcao']
