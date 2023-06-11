import random
# 1) Faça um programa que mostre a tabuada de um numero até o usuario não querer mais

while True:
    num = int(input('Digite um número para saber sua tabuada: '))
    for c in range(0, 11):
        print(f'{num} * {c} = {num * c}')
    print('-' * 30)
    q = str(input('Quer continuar? [S/N] '))
    if q in 'Nn':
        break

# 2) Faça um programa que calcule o numero ao quadrado até o usuario digitar uma string, zero ou um numero negativo

while True:
    n = input('Digite um valor: ')
    if n[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        n = int(n)
        if n <= 0:
            break
        else:
            print(f"O número {n} ao quadrado é: {n**2}")
    else:
        break

# 3) Atualize o ex 2 da lista 1 e adicione while ou for para msg de erro

altura = float(input('Digite sua altura em M: '))
sexo = input('Digite o seu sexo [F/M]: ')[0]

while sexo not in "FfMm":
    print('-'*30)
    print('Valor invalido!')
    print('-' * 30)
    sexo = input('Digite o seu sexo [F/M]: ')[0]

if sexo == "M":
    peso = (72.7 * altura) - 58
    print(f'O seu peso ideal sendo do sexo masculino é: {peso:.2f}Kg')
else:
    peso = (62.1 * altura) - 44.7
    print(f'O seu peso ideal sendo do sexo feminino é: {peso:.2f}Kg')


# 4) Atualize o ex 4 da lista 1 e adicione while ou for e um sistema de pontos no final que mostre:
    #quantas partidas teve;
    #quantas vezes a cpu ganhou;
    #quantas vezes o user ganhou;
    #quantas vezes houve empate;

print('-' * 30)
contador_u = contador_c = empate = cont = 0
user = ' '
cpu = ' '
question = ' '
while question not in 'Nn':
    user = str(input('''MENU:
[ 1 ] Para Pedra
[ 2 ] Para Papel
[ 3 ] Para Tesoura
Digite: '''))

    while user not in '123':
        print('-' * 30)
        print('Valor invalido!')
        print('-' * 30)
        user = str(input('''MENU:
[ 1 ] Para Pedra
[ 2 ] Para Papel
[ 3 ] Para Tesoura
Digite: '''))

    escolha = ['Pedra', 'Papel', 'Tesoura']
    cpu = random.choice(escolha)

    if user == '1':
        user = 'Pedra'
        if user == cpu:
            print('Empate!')
            print('-' * 30)
            empate += 1
            cont += 1

        elif cpu == 'Tesoura':
            print('Parabéns! Você ganhou de mim!')
            contador_u += 1
            print('-' * 30)
            cont += 1

        elif cpu == 'Papel':
            print('Eu ganhei de você!')
            contador_c += 1
            print('-' * 30)
            cont += 1

    if user == '2':
        user = 'Papel'
        if user == cpu:
            print('Empate!')
            print('-' * 30)
            empate += 1
            cont += 1

        elif cpu == 'Tesoura':
            print('Eu ganhei de você!')
            contador_c += 1
            print('-' * 30)
            cont += 1

        elif cpu == 'Pedra':
            print('Parabéns! Você ganhou de mim!')
            contador_u += 1
            print('-' * 30)
            cont += 1

    if user == '3':
        user = 'Tesoura'
        if user == cpu:
            print('Empate!')
            print('-' * 30)
            empate += 1
            cont += 1

        elif cpu == 'Pedra':
            print('Eu ganhei de você!')
            contador_c += 1
            print('-' * 30)
            cont += 1

        elif cpu == 'Papel':
            print('Parabéns! Você ganhou de mim!')
            contador_u += 1
            print('-' * 30)
            cont += 1

    question = str(input("Quer continuar? [S/N] "))[0]
    print('-' * 30)
    while question not in 'SsNn':
        print('Valor invalido!')
        print('-' * 30)
        question = str(input("Quer continuar? [S/N] "))[0]
        print('-' * 30)

print(f'''RESULTADO FINAL:
PARTIDA(S) JOGADA(S) {cont};
EMPATE(S) {empate};
CPU {contador_c} PONTO(S);
USER {contador_u} PONTO(S).''')
print('-' * 30)


# 5) Atualize o ex 5 da lista 1 e adicione while ou for

title = 'Calculadora'
print('=-' * 15)
print(f'{title:^30}')
print('=-' * 15)
title = 'MENU'
print(f'{title:^30}')
p = ' '
while p not in 'Ss':
    print('''
    [ 1 ] Adição;
    [ 2 ] Subtração;
    [ 3 ] Divisão [Por inteiros];
    [ 4 ] Multiplicação;
    [ 5 ] Exponenciação
    [ 6 ] Raiz quadrada [Cubica]
    [ 7 ] Conversão [Hexadecimal / Octadecimal / Binário]''')
    p = input('Digite [S para sair]: ')

    if p == '1':
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
        print(f'A soma entre os números {n1} e {n2} é: {n1 + n2}.')
    if p == '2':
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
        print(f'A subtração entre os números {n1} e {n2} é: {n1 - n2}.')
    if p == '3':
        title = 'SUB-MENU: DIVISÃO'
        print('=-' * 15)
        print(f'{title:^30}')
        print('[ 1 ] Divisão normal')
        print('[ 2 ] Divisão por inteiros')
        print('[ 3 ] Resto da divisão')
        p = int(input('Digite: '))

        if p == 1:
            n1 = float(input('Digite o 1º valor: '))
            n2 = float(input('Digite o 2º valor: '))
            print(f'A divisão entre os números {n1} e {n2} é: {n1 / n2}.')
            print(f'O resto da divisão foi: {n1 % n2}.')
        if p == 2:
            n1 = float(input('Digite o 1º valor: '))
            n2 = float(input('Digite o 2º valor: '))
            print(f'A divisão inteira entre os números {n1} e {n2} é: {n1 // n2}')

    if p == '4':
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
        print(f'A multiplicação entre os números {n1} e {n2} é: {n1 * n2}')

    if p == '5':
        title = 'SUB-MENU: EXPONENCIAÇÃO'
        print('=-' * 15)
        print(f'{title:^30}')
        print('[ 1 ] Exponenciação por ele mesmo')
        print('[ 2 ] Exponenciação por um número personalizado')
        p = int(input('Digite: '))
        if p == 1:
            n1 = float(input('Digite um valor: '))
            print(f'A exponenciação do número {n1} é: {n1 ** n1}')

        if p == 2:
            n1 = float(input('Digite o 1º valor: '))
            n2 = float(input('Digite o 2º valor: '))
            print(f'A exponenciação do número {n1} com o expoente {n2} é: {n1 ** n2}')

    if p == '6':
        title = 'SUB-MENU: RAIZ'
        print('=-' * 15)
        print(f'{title:^30}')
        print('[ 1 ] Raiz quadrada')
        print('[ 2 ] Raiz cubica')
        p = int(input('Digite: '))
        if p == 1:
            n1 = float(input('Digite um valor: '))
            print(f'A raiz quadrada de {n1} é: {n1 ** (1 / 2)}')
        if p == 2:
            n1 = float(input('Digite um valor: '))
            print(f'A raiz cubica de {n1} é: {n1 ** (1 / 3)}')

    if p == '7':
        title = 'SUB-MENU: CONVERSÃO'
        print('=-' * 15)
        print(f'{title:^30}')
        print('[ 1 ] Hexadecimal')
        print('[ 2 ] Octadecimal')
        print('[ 3 ] Binário')
        p = int(input('Digite: '))
        if p == 1:
            n1 = int(input('Digite um valor: '))
            print(f'O valor de {n1} em hexadecimal é: {hex(n1)[2:]}')

        if p == 2:
            n1 = int(input('Digite um valor: '))
            print(f'O valor de {n1} em octadecimal é: {oct(n1)[2:]}')

        if p == 3:
            n1 = int(input('Digite um valor: '))
            print(f'O valor de {n1} em binário é: {bin(n1)[2:]}')