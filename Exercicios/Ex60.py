n = int(input('Digite um número: '))
j = n-1
m = n
while j != 1:
    n = n*j
    j -= 1

print("O fatorial de {} é: {}".format(m, n))