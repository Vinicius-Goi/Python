maior = 0
menor = 0
for c in range(5):
    c += 1
    peso = float(input(f'Digite o peso (Kg) da {c}º pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))
