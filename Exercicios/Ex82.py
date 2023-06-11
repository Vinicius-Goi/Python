lista = list()
lista_p = []
lista_i = list()

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n %2  == 0:
        lista_p.append(n)
    else:
        lista_i.append(n)

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-'*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_p}')
print(f'A lista de impares é {lista_i}')