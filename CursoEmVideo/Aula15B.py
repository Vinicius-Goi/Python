#help(print)
#print(input.__doc__)
"""
def contador(i,f,p):
    '''
    Faz uma contagem e mostra na tela.
    Para i: inicio da contagem
    Para f: fim da contagem
    Para p: passo da contagem
    return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c+=p
    print('FIM!')


contador(2,10,2)

help(contador)
"""
'''
def somar(a=0,b=0,c=0):
    """
    Faz uma soma entre A B e C e apresenta na tela.
    Para a: 1º valor
    Para b: 2º valor
    Para c: 3º valor
    return: sem retorno
    """
    s = a+b+c
    print(f'A soma vale {s}')


somar(3,2,5)
somar(8,4)
somar()
'''
'''
def teste():
    global n # faz a variavel global perder seu valor inicial e substitui pelo valor definido na local
    n = 9 #ecopo local / variavel local
    x = 8 #escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa Principal
n = 2 #escopo global / variavel global
print(f'No programa principal, n vale {n}')
teste()
'''
'''
def somar(a=0,b=0,c=0):
    s = a+b+c
    return s

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
r4 = somar()
print(f'Meus cálculos deeram {r1}, {r2}, {r3} e {r4}.')
'''
