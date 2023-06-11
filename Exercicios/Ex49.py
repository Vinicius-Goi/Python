n = int(input('Digite a tabuada desejada: '))
for c in range(0, 10+1):
    calc = n*c
    print('{}*{} = {}'.format(n, c, calc))