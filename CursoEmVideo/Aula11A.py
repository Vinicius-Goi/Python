'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
print('Acabou')
cont = 1
while True:
    print(cont, '-> ', end='')
print('Acabou')'''
'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''
nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}.') #PYTHON 3.6+
print(f'O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}.') #PYTHON 3.6+
print(f'O {nome:->20} tem {idade} anos e ganha R${salario:.2f}.') #PYTHON 3.6+
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}.') #PYTHON 3.6+
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}.') #PYTHON 3.6+
#print('O {} tem {} anos e ganha R${}.'.format(nome, idade, salario)) #PYTHON 3
#print('O %s tem %d anos e ganha %f.' % (nome, idade, salario)) #PYTHON 2