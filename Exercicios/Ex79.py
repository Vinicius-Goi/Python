lista = []
while True:
    p = int(input('Digite um valor: '))
    if p not in lista:
        lista.append(p)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-'*30)
lista.sort()
print(f'Você digitou os valores {lista}')