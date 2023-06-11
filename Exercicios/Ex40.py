'''n1 = float(input("Digite a primeira nota: "))
i = False
while not i:
    try:
        if n1 <= 10:
            i = True
        else:
            print("-"*40)
            print("\033[4;31mDigite um Valor Válido!\033[m")
            print("-"*40)
            n1 = float(input("Digite a primeira nota: "))
    except ValueError:
        print("-"*40)
        print("\033[4;31mDigite um Valor Válido!\033[m")
        print("-"*40)
        n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
i = False
while not i:
    try:
        if n2 <= 10:
            i = True
        else:
            print("-"*40)
            print("\033[4;31mDigite um Valor Válido!\033[m")
            print("-"*40)
            n2 = float(input("Digite a segunda nota: "))
    except ValueError:
        print("-"*40)
        print("\033[4;31mDigite um Valor Válido!\033[m")
        print("-"*40)
        n2 = float(input("Digite a segunda nota: "))

med = (n1+n2)/2
if med < 5:
    print('-'*40)
    print('Você foi \033[4;31mREPROVADO(A)!\033[m')
    print('-'*40)
elif med >= 5 and med <=6.9:
    print('-'*40)
    print('Você está de \033[4;33mRECUPERAÇÃO!\033[m')
    print('-'*40)
else:
    print('-'*40)
    print('Você foi \033[4;32mAPROVADO(A)!\033[m')
    print('-'*40)'''
#Resolução Guanabara