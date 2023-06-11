import random

# 1) Faça um programa que leia o nome completo e apresente uma saudação e o nome completo.

nome = input('Digite seu nome completo: ').title()
print(f'Olá {nome}! Prazer em te conhecer!')


# 2) Faça um programa que leia a altura (em M) e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando
# as seguintes formulas: Para mulheres: (62.1 * altura) - 44.7; Para homens: (72.7 * altura) - 58.

altura = float(input('Digite sua altura em M: '))
sexo = input('Digite o seu sexo [F/M]: ').upper()[0]

if sexo == "M":
    peso = (72.7 * altura) - 58
    print(f'O seu peso ideal sendo do sexo masculino é: {peso:.2f}Kg')
elif sexo == "F":
    peso = (62.1 * altura) - 44.7
    print(f'O seu peso ideal sendo do sexo feminino é: {peso:.2f}Kg')
else:
    print('Digite um valor válido!')


# 3) Faça um programa que leia uma quantidade de tempo em minutos e apresente no formato de horas.  Exemplo:: 80 min
# = 1:20 hs.

tempo = int(input('Digite a quantidade de tempo em \033[1mminutos\033[m: '))

# metodo 1:
horas = tempo // 60
minutos = tempo % 60
print(f'Convertendo {tempo} minutos para horas fica: {horas}H:{minutos:02d}MIN')

# metodo 2:
horas, minutos = divmod(tempo, 60)
print(f'Convertendo {tempo} minutos para horas fica: {horas}H:{minutos:02d}MIN')

# metodo 3:
horas = (tempo // 60) + (tempo % 60) / 100
print(f'Convertendo {tempo} minutos para horas fica: {horas:.2f}h'.replace('.', ':'))


# 4) Faça um jogo de pedra, papel e tesoura (que mostre quantos pontos o jogador fez no final.)
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

    elif cpu == 'Tesoura':
        print('Parabéns! Você ganhou de mim!')
        print('-' * 30)


    elif cpu == 'Papel':
        print('Eu ganhei de você!')
        print('-' * 30)


if user == '2':
    user = 'Papel'
    if user == cpu:
        print('Empate!')
        print('-' * 30)

    elif cpu == 'Tesoura':
        print('Eu ganhei de você!')
        print('-' * 30)

    elif cpu == 'Pedra':
        print('Parabéns! Você ganhou de mim!')
        print('-' * 30)

if user == '3':
    user = 'Tesoura'
    if user == cpu:
        print('Empate!')
        print('-' * 30)

    elif cpu == 'Pedra':
        print('Eu ganhei de você!')
        print('-' * 30)

    elif cpu == 'Papel':
        print('Parabéns! Você ganhou de mim!')
        print('-' * 30)


# 5) Faça uma calculadora, nessa calculadora deve ter:
# 1. Uma interface simples (usando o proprio terminal);
# 2. Calcular:
# adição;
# subtração;
# divisão;
# multiplicação;
# divisão por inteiros;
# divisão com resto;
# exponenciação;
# raiz quadrada;
# raiz cubica;
# mostre o 1º valor em hexadecimal, binario e octadecimal

title = 'Calculadora'
print('=-' * 15)
print(f'{title:^30}')
print('=-' * 15)
title = 'MENU'
print(f'{title:^30}')
print('''
[ 1 ] Adição;
[ 2 ] Subtração;
[ 3 ] Divisão;
[ 4 ] Multiplicação;
[ 5 ] Exponenciação
[ 6 ] Raiz;
[ 7 ] Conversão''')
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

    if p == 2:
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
        print(f'A divisão inteira entre os números {n1} e {n2} é: {n1 // n2}')

    if p == 3:
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
        print(f'O resto da divisão foi: {n1 % n2}.')

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
