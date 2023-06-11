#MINHA RESOLUÇÃO

i = quant = homi = muie = 0
while True:
    i = int(input('Quantos anos você tem? '))
    s = ' '
    while s not in 'mf':
        s = str(input('Qual é o seu sexo? [F/M] ')).strip().lower()[0]
    if i >= 18:
        quant += 1
    if s == 'm':
        homi += 1
    if s == 'f' and i <= 20:
        muie += 1
    p = ' '
    while p not in 'SN':
        p = input('Você quer continuar cadastrando? [S/N] ').strip().upper()[0]
    if p == 'N':
        break
print(f'{quant} pessoas são tem ou são maiores que 18 anos.')
print(f'{homi} homens cadastrados.')
print(f'{muie} mulheres são menores que 20 anos.')

#RESOLUÇÃO GUANABARA
'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')'''