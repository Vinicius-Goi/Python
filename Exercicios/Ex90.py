info = dict()
info['Nome'] = input('Nome: ').title()
info['Média'] = float(input(f'Média de {info["Nome"]}: '))
if info['Média'] >= 7:
    info['Situação'] = 'Aprovado(a)!'
else:
    info['Situação'] = 'Reprovado(a)!'

for k, v in info.items():
    print(f'{k} é igual a {v}')