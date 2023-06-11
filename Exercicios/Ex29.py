'''
Minha resolução:
p = float(input('Qual é a sua velocidade?'))
if p > 80:
    val = (p-80)*7
    print('Você foi multado! Pague R${:.2f}'.format(val))
else:
    print('Você está na velocidade certa!')
'''
#Resolução do Guanabara
velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa de R${:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
