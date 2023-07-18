from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo == 1

    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)
    
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(c, end=' ')
            sleep(0.5)
            c += passo
        print('FIM!')

    else:
        c = inicio
        while c >= fim:
            print(c, end=' ')
            sleep(0.5)
            c -= passo
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)