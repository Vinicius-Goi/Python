'''
Minha resolução
s = float(input('Qual é o seu salário atual? R$'))
if s > 1250:
    c = s + (s * 10 / 100)
    print('Seu salário será de: R${:.2f} após o aumento de 10%'.format(c))
if s <= 1250:
    c = s + (s * 15 / 100)
    print('Seu salário será de: R${:.2f} após o aumento de 15%'.format(c))
'''
#Resolução do Guanabara
s = float(input('Qual é o salário do funcionário? '))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('Quem ganhava R${:.2} passa a ganhar R${:.2} agora.'.format(s, novo))