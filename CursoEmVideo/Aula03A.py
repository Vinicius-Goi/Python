nome = input('Qual é o seu nome?')
print('Prazer em te conhecer {:=^20}!'.format(nome))
#Operações aritméticas
# + para adição: 5 + 2 == 7
# - para subtração: 5 - 2 == 3
# * para multiplicação: 5 * 2 == 10
# / para divisão: 5 / 2 == 2.5
# ** para potência: 5 ** 2 == 25 (pow (5,2))
# // para divisão inteira: 5 // 2 == 2
# % para resto da divisão (módulo): 5 % 2 == 1

#Ordem de precedência
# 1º: ()
# 2º: **
# 3º: *, /, //, %
# 4º: +, -
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale: {} \nA multiplicação entre esses números é:{} \nSua divisão vale:{:.3f} \nSua divisão inteira vale:{} \nA exponenciação vale:{}'.format(s, m, d, di, e))

