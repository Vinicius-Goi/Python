n_preco = float(input('Digite o preço do produto: '))
pag = int(input('''Digite:
1. Para pagamento à vista em dinheiro/cheque.
2. Para pagamento à vista no cartão.
3. Para pagamento em até 2x no cartão.
4. Para pagamento em até 3x ou mais no cartão.
'''))
if pag == 1:
    calc = n_preco-(n_preco * 10 / 100)
    print('Por conta dos 10% de desconto você pagará R${:.2f}'.format(calc))
elif pag == 2:
    calc = n_preco-(n_preco * 5 / 100)
    print('Por conta dos 5% de desconto você pagará R${:.2f}'.format(calc))
elif pag == 3:
    print('Você pagará o preço normal do produto R${:.2f}'.format(n_preco))
else:
    calc = n_preco+(n_preco * 20 /100)
    print('Você terá um acrescimo de 20% na sua compra, pague R${:.2f}'.format(calc))