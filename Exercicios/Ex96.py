def area(larg, comp):
    a = larg*comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')


# Programa Principal
print(f'{"Controle de Terrenos":^20}')
print('-'*20)

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)