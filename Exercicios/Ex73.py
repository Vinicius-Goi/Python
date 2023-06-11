campeoes = 'Palmeiras', 'Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Corinthians', 'Palmeiras', 'Corinthians', 'Cruzeiro', 'Cruzeiro', 'Fluminense', 'Corinthians', 'Fluminense', 'Flamengo', 'São Paulo', 'São Paulo', 'São Paulo', 'Corinthians', 'Santos', 'Cruzeiro', 'Santos'
print('-='*20)
print(f'Lista de times do Brasileirão: {campeoes}')
print('-='*20)
print(f'Os 5 primeiros são {campeoes[:5]}')
print('-='*20)
print(f'Os 4 últimos são {campeoes[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(campeoes)}')
print('-='*20)
if 'Chapecoense' in campeoes:
    print(f'O time da Chapecoense está na {campeoes.index("Chapecoense")}ª posição')
else:
    print('O time Chapecoense não está em nenhuma posição')

