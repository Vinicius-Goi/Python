#Jeito errado
n1 = input('Digite o primeiro número da somatória:')
n2 = input('Digite o segundo númeor da somatória:')
soma = n1+n2
print('O resultado da soma é:',soma) #Jeito tradicional

#Jeito certo
n1 = int(input('Digite o primeiro número da somatória:'))
n2 = int(input('Digite o segundo númeor da somatória:'))
soma = n1+n2
print('O resultado da soma é: {}'.format(soma)) #Jeito bonito