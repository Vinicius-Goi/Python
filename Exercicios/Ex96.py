def area(larg, alt):
    a = larg*alt
    print(f'A área de um terreno {larg} x {alt} é de {a}m².')


print(f'{"Controle de Terrenos":^20}')
print('-'*20)

larg = float(input('LARGURA (m): '))
alt = float(input('COMPRIMENTO (m): '))
area(larg, alt)