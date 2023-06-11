'''from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = sqrt((co**2)+(ca**2))
print('O valor da hipotenusa é: {:.2f}'.format(hi))'''
'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co**2+ca**2)**(1/2)
print('O valor da hipotenusa é: {:.2f}'.format(hi))'''
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}'.format(hi))