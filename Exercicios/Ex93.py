jogador = {}
partidas = list()

jogador['nome'] = input('Nome do jogador: ')
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
for i in range(0, quant):
    partidas.append(int(input(f"Quantos gols na partida {i}? ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*30)
print(jogador)
print('-='*30)

for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f"=> Na partida {i}, fez {v}.")
print(f'Foi um total de {jogador["total"]} gols.')