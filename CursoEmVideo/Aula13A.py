'''lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
#-
lanche[3] = 'picolé'
print(lanche)
#-
lanche.append('cookie')
print(lanche)
#-
lanche.insert(0, 'hot-dog')
print(lanche)
#-
#del lanche[3]
lanche.pop(3)
lanche.pop()
if 'pizza' in lanche:
    lanche.remove('pizza')#.remove remove somente indicando o objeto, n pode remover usando o indice
print(lanche)
'''
'''
#-
valores = list(range(4,11))
print(valores)
print('-'*30)#------------
valores.insert(3, 4)
print(valores)
valores.remove(4)
print(valores)
print('-'*30)#------------
valor = [8,2,5,4,9,3,0]
print(valor)
print('-'*30)#------------
valorr = [8,2,5,4,9,3,0]
valorr.sort()
print(valorr)
print('-'*30)#------------
valoress = [8,2,5,4,9,3,0]
valoress.sort(reverse=True)
print(valoress)
print('-'*30)#-
print(f'Essa lista tem {len(valor)} elementos.')
print('-'*30)#------------
if 10 in valor:
    valor.remove(10)
    print(valor)
else:
    print('Não achei o número 10')
print('-'*30)#------------
if 9 in valor:
    valor.remove(9)
    print(valor)
else:
    print('Não achei o número 9')'''
'''#-
valores = []
valores.append(5)
valores.append(9)
valores.append(4)'''

'''
for v in valores:
    print(f'{v}...', end='')
'''
'''valores = []
for cont in range(0,6):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')'''
'''a = [2,3,4,7]
b = a[:]#usando o [:] vc irá criar uma copia e n uma ligação entre as listas
b[2] = 8 #ele troca tanto na lista a quanto na lista b
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
