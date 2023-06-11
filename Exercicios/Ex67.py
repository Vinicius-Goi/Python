#Minha resolução
cont = n = tabuada = 0
while True:
    n = int(input('Digite um número para saber a sua tabuada: '))
    print('-=' * 20)
    if n < 0:
        break

    while True:
        print(f'{n} * {cont} = {n * cont}')
        cont += 1

        if cont == 11:
            cont = 0
            break
print('Tabuada \033[4:31mENCERRADA\033[m, volte sempre!')

'''while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')'''
