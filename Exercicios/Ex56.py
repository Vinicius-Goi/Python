somaidade = 0
med = 0
maioridade = 0
nomevelho = ''
tmulher20 = 0
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    n = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexp [M/F]: ')).strip
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = n
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = n
    if sexo in 'Ff' and idade > 20:
        tmulher20 += 1
med = somaidade/4
print('A média de idade é de {} anos'.format(med))
print('O homem mais velho tem {} e se chama {}'.format(maioridade, nomevelho))
print('Ao todo são {} muilheres com menos de 20 anos'.format(tmulher20))