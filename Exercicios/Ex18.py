'''import math
a = float(input('Digite o valor de um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno de {} equivale a: {:.2f}\nO cosseno de {} equivale a: {:.2f}\nA tangente de {} equivale a: {:.2f}'.format(a, s, a, c, a, t))'''
from math import radians, sin, cos, tan
a = float(input('Digite o valor de um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O seno de {} equivale a: {:.2f}\nO cosseno de {} equivale a: {:.2f}\nA tangente de {} equivale a: {:.2f}'.format(a, s, a, c, a, t))