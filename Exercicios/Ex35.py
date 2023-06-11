'''
Minha resolução
n1 = float(input('Digite um valor de uma reta: '))22
n2 = float(input('Digite um valor de outra reta: '))
n3 = float(input('Digite mais um valor de reta: '))
if n1 + n2 > n3:
    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')
'''
#Resolução do Guanabara
print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima não podem formar um triangulo')