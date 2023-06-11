from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções
0. PEDRA
1. PAPEL
2. TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('\033[4;33mEMPATE!\033[m')
    elif jogador == 1:
        print('JOGADOR \033[4;32mVENCE!\033[m')
    elif jogador == 2:
        print('COMPUTADOR \033[4;32mVENCE!\033[m')
    else:
        print('\033[4;31mJOGADA INVALIDA!\033[m')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR \033[4;32mVENCE!\033[m')
    elif jogador == 1:
        print('\033[4;33mEMPATE!\033[m')
    elif jogador == 2:
        print('JOGADOR \033[4;32mVENCE!\033[m')
    else:
        print('\033[4;31mJOGADA INVALIDA!\033[m')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR \033[4;32mVENCE!\033[m')
    elif jogador == 1:
        print('COMPUTADOR \033[4;31mVENCE\033[m')
    elif jogador == 2:
        print('\033[4;33mEMPATE!\033[m')
    else:
        print('\033[4;31mJOGADA INVALIDA!\033[m')