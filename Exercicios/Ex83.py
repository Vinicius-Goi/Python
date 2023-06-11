exp = str(input('Digite a expressão: '))
lista = list()
for sim in exp:
    if sim == '(':
        lista.append('(')
    elif sim == ')':
        if len(lista) > 0:
            lista.pop() #removendo o ultimo elemento da lista
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está invalida!')