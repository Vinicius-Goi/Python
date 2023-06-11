titulo = 'Conversor de bases numéricas'

print('-=-'*20)
print(titulo.center(55).title())
print('-=-'*20)
nome = str(input('Qual é o seu nome? ')).strip().lower().capitalize()
q = int(input('Olá {}! Selecione: \n1 para a base binária\n2 para a base octal\n3 para a base hexadecimal\n'.format(nome)))
if q == 1:
    num = int(input('Digite um número: '))
    bi = bin(num) [2:]
    print('O número digitado em binário é: {}'.format(bi))
elif q == 2:
    num = int(input('Digite um número: '))
    oc = oct(num) [2:]
    print('O número digitado em octal é: {}'.format(oc))
elif q == 3:
    num = int(input('Digite um número: '))
    he = hex(num) [2:]
    print('O número digitado em hexadecimal é: {}'.format(he))
else:
    print('\033[4;31mOPÇÃO INVALIDA! TENTE NOVAMENTE!\033[m')