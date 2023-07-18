'''def mostraLinha():
    print('-'*40)


mostraLinha()
print('     Sistema de Alunos      ')
mostraLinha()
mostraLinha()
print('     Cadastro de Funcionários       ')
mostraLinha()
mostraLinha()
print('     ERRO DO SISTEMA       ')
mostraLinha()
'''
'''
def mensagem(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)


mensagem('SISTEMA DE ALUNOS')
'''
'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
'''

'''
def soma(a, b):
    print(f'A é igual a {a} e B é igual a {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print()

# Programa Principal
soma(a=4,b=5)
soma(b=8,a=9)
soma(b=2,a=1)
'''
'''
def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM!')
    print(f'Recebi os valores {num} e são ao todo {len(num)} números')
    print()


contador(2,1,7)
contador(8,0)
contador(4,4,5,6,7)
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)