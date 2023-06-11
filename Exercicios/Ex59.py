n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
q = 0
while q != 5:
    q = int(input('''
    Digite:
    [1] Para somar;
    [2] Para multiplicar;
    [3] Para saber o maior valor
    [4] Para novos números;
    [5] Para sair do Programa.
    '''))
    if q == 1:
        print('A soma entre o número {} e {} é igual à {}'.format(n1, n2, n1+n2))
    elif q == 2:
        print('A multiplicação entre o número {} e {} é igual à {}'.format(n1, n2, n1*n2))
    elif q == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        elif n2 > n1:
            print('O maior número é {}'.format(n2))
        else:
            print('Os dois números são iguais!')
    elif q == 4:
        print("Informe novamente os números:")
        n1 = float(input('Digite o 1º número: '))
        n2 = float(input('Digite o 2º número: '))
    elif q == 5:
        print("Finalizando...")
    else:
        print("Opção invalida, tente novamente!")
print("Fim do Programa, volte sempre!")