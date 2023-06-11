lista = list()
cont = 0
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    lista.append(n)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-'*30)
print(f'Você digitou {cont} elementos') #len(lista)
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')