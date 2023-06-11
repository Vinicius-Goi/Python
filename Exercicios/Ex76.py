listagem = 'Lápis', 1.75, \
           'Borracha', 2,\
           'Caderno', 15.90,\
           'Estojo', 30,\
           'Mochila', 80.25,\
           'Canetas', 25.67,\
           'Livros', 120.50
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)