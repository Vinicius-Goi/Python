from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for i in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(i)))
    idade = atual - nasc
    if idade >= 18:
        total_maior += 1

    else:
        total_menor += 1
print('Aqui temos: \n{} pessoa(s) de maior\n{} pessoa(s) de menor'.format(total_maior, total_menor))