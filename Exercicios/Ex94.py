pessoa = dict()
pessoas = list()
soma, media = 0, 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')

    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())

    while True:
        resp = input("Quer continuar? [S/N]").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'S':
        break

print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')

for p in pessoas:
    if p['sexo'] in 'F':
        print(f"{p['nome']}", end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')

for p in pessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()

print("<<ENCERRADO>>")