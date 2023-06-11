#\033[style; text; back m]
'''
Style:0, 1, 4 e 7
0: none
1: Bold
4: Underline
7: Negativo

Text:30 até 37
30: branco
31: vermelho
32: verde
33: amarelo
34: azul
35: roxo
36: ciano
37: cinza

Background: 40 até 47
40: branco
41: vermelho
42: verde
43: amarelo
44: azul
45: roxo
46: ciano
47: cinza

\033[0; 30; 41m
\033[4; 33; 44m
\033[1; 35; 43m
\033[30; 42m
\033[m
\033[7;30m

'''
print('\033[1;30;45mHello world!\033[m')
print('\033[4;35;40mHello world!\033[m')
print('\033[7;31;47mHello world!\033[m')
print('\033[0;30;47mHello world!')
a = 14
b = 41
print('Os valores sao: \033[30;45m{}\033[m e \033[35;40m{}\033[m'.format(a, b))
print('Os valores sao: \033[1;35m{}\033[m e \033[7;35m{}\033[m'.format(a, b))

#Brincando com as cores no terminal :)
nome = str(input('Seu nome: '))
nome = nome.strip().capitalize()
cor = str(input('Entre, preto, vermelho, verde, amarelo, azul, roxo, ciano e cinza, qual a sua cor favorita? '))
cor = cor.strip().upper()
if cor == 'PRETO':
    print('Ola! Muito prazer em te conhecer {}{}{}!'.format('\033[4;30m', nome, '\033[m'))
elif cor == 'VERMELHO':
    print('Ola! Muito prazer em te conhecer {}{}{}!'.format('\033[4;31m', nome, '\033[m'))
elif cor == 'VERDE':
    print('Ola! Muito prazer em te conhecer {}{}{}!'.format('\033[4;32m', nome, '\033[m'))
elif cor == 'AMARELO':
    print('Ola! Muito prazer em te conhecer {}{}{}!'.format('\033[4;33m', nome, '\033[m'))
elif cor == 'AZUL':
    print('Ola! Muito prazer em te conhecer {}{}{}!'.format('\033[4;34m', nome, '\033[m'))
elif cor == 'ROXO':
    print('Ola! Muito prazer em te conhecer {}{}{}!'.format('\033[4;35m', nome, '\033[m'))
elif cor == 'CIANO':
    print('Ola! Muito prazer em te conhecer {}{}{}!'.format('\033[4;36m', nome, '\033[m'))
else:
    print('Ola! Muito prazer em te conhecer {}{}{}!'.format('\033[4;37m', nome, '\033[m'))







