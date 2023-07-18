from time import sleep
def contador(inicio, fim, passo):
    print('-='*30)
    print('Contagem de {} até {} de {} em {}')
    if inicio < fim:
        for c in range(inicio, fim, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')

    else:
        for c in range(fim, inicio, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')

contador(1, 11, 1)
contador(10, -1, -2)

print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)