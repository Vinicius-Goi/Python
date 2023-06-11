'''Condições simples e compostas
Estrutura sequencial - sequencias q não se pode mudar tanto, se não podemos quebrar o codigo
Identação - 'tab'
Estrutura condicional - if

if (condicao):
    bloco true
else:
    bloco false

'''
'''
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 5:
    print('Carro novinho!')
else:
    print('Carro tá veio hein!')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novin!'if tempo <=5 else'Carro tá veio hein fi!')
print('--FIM--')
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
#print('Parabéns! Você foi aprovado, até ano que vem! :)' if m >= 6 else 'Bahh, sua nota precisa melhorar, que pena, até semana que vem! >:)')
if m >= 6:
    print('Parabéns! Você foi aprovado, até ano que vem! :)')
else:
    print('Bahh, sua nota precisa melhorar, que pena, até semana que vem! >:)')
