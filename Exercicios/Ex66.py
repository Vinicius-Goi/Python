n = cont = soma = 0
while True:
    n = int(input('Digite algum número [999 para \033[4;31mPARAR\033[m]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')

