s_n = "S"
cont = soma = med = maior = menor = 0
while s_n in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    s_n = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
med = soma / cont
print("""Você digitou {} números e a média entre eles foi: {:.2f}
O maior número foi {} e o menor foi {}""".format(cont, med, maior, menor))

"""resp = "S"
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
        if quant == 1:
        maior = menor = n
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quant
print("Você digitou {} números e a média foi {}".format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))"""
