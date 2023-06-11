'''
Minha resolução:
v1 = float(input('Primeiro número: '))
v2 = float(input('Segundo número: '))
v3 = float(input('Terceiro número: '))
if v1 > v2 and v1 > v3:
    print('O maior número é: {}'.format(v1))
if v2 > v1 and v2 > v3:
    print('O maior número é: {}'.format(v2))
if v3 > v1 and v3 > v2:
    print('O maior número é: {}'.format(v3))
if v1 < v2 and v1 < v3:
    print('O menor número é: {}'.format(v1))
if v2 < v1 and v2 < v3:
    print('O menor número é: {}'.format(v2))
if v3 < v1 and v3 < v2:
    print('O menor número é: {}'.format(v3))
'''
#Resolução Guanabara
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))
menor = a
if b <a and b<c:
        menor = b
if c<a and c<b:
    menor = c
maior = c
if a>c and a>b:
    maior = a
if b>c and b>a:
    maior = b
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
