peso_pesce = float(input("Digite quantos Kg de peixes foram pegos: "))
if peso_pesce >= 50:
    peso_pesce *= 4
    print(f'Você foi multado em R${peso_pesce:.2f}')
else:
    print("Você não foi multado")