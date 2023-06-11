f = str(input('Digite uma frase: ')).strip().upper()
separado = f.split()
junto = ''.join(separado)
inverso = ''
#inverso = junto[::-1]
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Essa frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')