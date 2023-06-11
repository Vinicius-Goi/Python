# Módulos:
# import bebidas - Importa todas as bebidas
# from bebidas import obj- Importa determinada bebida

# math: import math - Importa diversas funções matematicas
# math: from match import factorial - Importa só o fatorial
# ceil - arredondamento para cima
# floor - arredondamento para baixo
# trunc - tira a virgula
# pow - potencia
# sqrt - raiz quadrada
# factorial - fatorial

# import math
# n = int(input('Digite um número: '))
# r = math.sqrt(n)
# print('A raiz de {} é igual a: {:.2f}'.format(n, r))
# print('O arredondamento para cima da raiz quadrada de {} é igual a: {}'.format(n, math.ceil(r)))
# print('O arredondamento para baixa da raiz quadrada de {} é igual a: {}'.format(n, math.floor(r)))
#import math
from math import sqrt, floor, ceil
n = int(input('Digite um número: '))
#r = math.sqrt(n)
r = sqrt(n)
print('A raiz de {} é igual a: {:.2f}'.format(n, r))
print('O arredondamento para cima da raiz quadrada de {} é igual a: {}'.format(n, ceil(r)))
print('O arredondamento para baixa da raiz quadrada de {} é igual a: {}'.format(n, floor(r)))