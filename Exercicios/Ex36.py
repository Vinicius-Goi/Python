c = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento? '))
p = c / (a * 12)
min = s * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(c, a), end='')
print(' a prestação será de R${:.2f}'.format(p))
if p <= min:
      print('Empréstimo pode ser \033[4;32mCONCEDIDO!\033[m')
else:
      print('Empréstimo \033[4;31mNEGADO!\033[m')