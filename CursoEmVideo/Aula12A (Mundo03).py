'''
Variavel simples:
lanche = 'Hamburguer'
lanche = 'Suco' #Elimina o hamburguer para atribuir o suco

Variavel composta - Existem 3 formas: Tuplas, listas, dicionários.
Tupla = () ou sem
Listas = []
Dicionarios = {}

Nessa aula vamos focar nas tuplas.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

lanche[0] = hamburguer
lanche[2] = pizza
lanche[3] = pudim
lanche[1] = suco

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata-Frita'

print(lanche)
print(sorted(lanche))

print(lanche[2])
print(lanche[0:2])
print(lanche[:3])
print(lanche[2:])
print(lanche[-1]) #ultimo elemento nesse caso, ele acessa o 'pudim', caso fosse -2, ele mostraria a pizza e assim vai.
print(lanche[-3:])
print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')#mesma coisa

for comida in lanche:
    print(f'Eu vou comer {comida}')#que esse
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')#e esse

print('Comi para caramba!')
'''
'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(a)
print(b)
print(c)
print(c.count(5))
print(c.index(8))#Qual pos está o num 8
print(c.index(4))#Qual pos está o num 4
print(c.index(2))#Qual pos está o num 2, em casos de num repetidos, ele mostrará somente a primeira ocorrencia
print(c.index(5, 1))#Qual pos está o num 5 a partir do indice 1'''
pessoa = ('Vinicius', 16, 'M', 1.79)
print(pessoa)
del(pessoa)#deletar a variavel pessoa

#AS TUPLAS SÃO IMUTÁVEIS, OU SEJA, N É POSSIVEL MUDAR ELA NO MEIO DO PROGRAMA, AO MENOS Q VC MUDE NOS CODIGOS


