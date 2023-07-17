from datetime import date

info = {}
info['nome'] = input('Nome: ')
info['anoNasc'] = int(input('Ano de Nascimento: '))
info['idade'] = date.today().year - info['anoNasc']
info['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if info['ctps'] != '0':
    info['contratação'] = int(input('Ano de Contratação: '))
    info['salário'] = float(input('Salário: R$'))
    info['aposentadoria'] = info['idade'] + ((info['contratação'] + 35) - date.today().year)
print('-='*30)

del info['anoNasc']
for k,v in info.items():
    print(f'- {k} tem o valor {v}')