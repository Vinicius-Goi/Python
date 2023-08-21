alt = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo [F/M]: ")
if sexo in "Ff":
    print(f'O peso ideal segundo sua altura (sendo uma mulher) é: {(62.1*alt)-44.7:.2f}Kg')
elif sexo in "Mm":
    print(f'A altura ideal segundo sua altura (sendo um homem) é: {(72.7*alt)-58:.2f}Kg')
else:
    print("Digite um valor válido!")