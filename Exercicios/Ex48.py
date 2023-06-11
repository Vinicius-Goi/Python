s = 0
for c in range(1, 500+1, 2):
    print(c, end=' ')
    if c % 3 == 0:
        s += c
print('''
\033[1mA somatória de todos os números multiplos de 3 é igual à: {}\033[m'''.format(s))
print('FIM')