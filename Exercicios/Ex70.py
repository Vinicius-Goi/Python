#MINHA RESOLUÇÃO

preco = total = quant = cont = 0
preco_1 = 1000
barato = ' '
while True:
    produtos = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço: R$'))
    p = ' '
    while p not in 'SN':
        p = input('Quer continuar? [S/N] ').strip().upper()[0]
    total += preco
    if preco >= 1000:
        quant += 1
    if preco < preco_1 or cont == 1:
        preco_1 = preco
        barato = produtos
    if p == "N":
        break
print('-='*20)
print(f'O total gasto será de R${total:.2f}')
print(f'{quant} produto(s) valem mais que R$1000,00')
print(f'O produto mais barato é o {barato} que custa R${preco_1:.2f}')


#RESOLUÇÃO GUANABARA
'''
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')'''