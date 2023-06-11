s = 0
for c in range(1, 6+1):
    n = int(input('Digite um número: '))
    if n %2 == 0:
        s += n
print('A soma dos valores PARES são: {}'.format(s))