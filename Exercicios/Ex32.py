'''
Minha resolução:
a = int(input('Coloque um ano para saber se ele é bissexto ou não: '))
if a % 4 == 0 and a % 100 != 0 or a%400== 0:
    print('O ano digitado ({}) é bissexto'.format(a))

else:
    print('O ano digitado ({}) não é bissexto'.format(a))
'''
#Resolução Guanabara
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
