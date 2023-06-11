#Minhas resoluções:
'''import random
p = 0
maquina = ['Par', 'Impar']
vitorias = 0
print('-='*10)
print('JOGO DA ADIVINHAÇÃO')
print('-='*10)
print('Estou pensando em par ou impar? Diga-me você:')
while True:
    p = int(input('''#[ 1 ] Para Par
#[ 2 ] Para Impar
'''))
    print('-'*10)
    escolha_maquina = random.choice(maquina)
    if p == 1:
        p = 'Par'
    if p == 2:
        p = 'Impar'
    if p == escolha_maquina:
        vitorias += 1
    if p != escolha_maquina:
        break

print(f'Que pena! Eu joguei {escolha_maquina} então você perdeu, mas ganhou de mim {vitorias} veze(s)!')'''


'''import random
p = 0
vitorias = 0
print('-='*10)
print('JOGO DA ADIVINHAÇÃO')
print('-='*10)
print('Estou pensando em um número par ou impar, digite um valor e veja se me vencerá:')
while True:
    p = int(input('Digite um valor: '))
    p_i = ' '
    while p_i not in 'PI':
        p_i = input('Par ou Impar? [P/I] ').strip().upper()[0]
    escolha = random.randint(0,10)
    print('-='*10)
    print(f'Você jogou {p} e o computador jogou {escolha}. Total foi {escolha + p} ', end='')
    print('DEU \033[1mPAR\033[m' if (p+escolha)%2 == 0 else 'DEU \033[1mIMPAR\033[m')

    if (p+escolha)%2 == 0 and p_i == "P":
        vitorias += 1
        print('-='*10)
        print('Você \033[32;4mvenceu\033[m! Jogue novamente...')
        print('-='*10)
    elif (p+escolha)%2 == 1 and p_i == "I":
        vitorias += 1
        print('-='*10)
        print('Você \033[32;4mvenceu\033[m! Jogue novamente...')
        print('-='*10)
    else:
        break

print('-='*10)
print(f'Você \033[31;4mperdeu\033[m, e venceu de mim {vitorias} vezes.')'''

#RESOLUÇÃO GUANABARA
'''from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total%2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total%2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')'''