"""
n = input('Digite o seu nome completo: ')
verificar = 'silva' in n.lower()
if verificar < 0:
    print('Seu nome contém Silva!')
else:
    print('Seu nome não contém Silva!')
"""
nome = str(input('Qual é o seu nome completo?'))
print('Seu nome é {} para Silva'.format('silva' in nome.lower()))

