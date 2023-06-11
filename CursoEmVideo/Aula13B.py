'''dados = list()
#pessoas = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
dados.append('Maria')
dados.append('19')
dados.append('João')
dados.append('32')

pessoas = [['Pedro',25], ['Maria',19],['João', 32]]
pessoas.append((dados[:])) #copia de dados e dando appeend
print(pessoas)
print(pessoas[0][0]) #Pedro
# #acessando o primeiro indice da primeira lista mais 'a frente' ou seja, pessoas, e depois acessando o indice da lista dados
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1]) #Maria, 19
#mostrando a lista toda'''
'''teste = list()
teste.append('Goi')
teste.append(16)
galera = list()
galera.append(teste[:]) #caso n seja feito uma copia ([:]) ele fara uma ligação e o que for mudado na primeira lista, vai mudar tbm na segunda
teste[0] = 'Miguel'
teste[1] = 16
galera.append(teste[:])
print(galera)
'''
'''galera = [['Goi', 16], ['Migg', 16], ['Here', 16], ['Igor', 16], ['Barone', 16], ['Michele', 16], ['Mayara', 16]]
print(galera[0][0]) #- Goi
print(galera[2][1]) #- 16
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')#p[0] para nome e p[1] para idade'''
galera = list()
dado = list()
totmai, totmen = 0, 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append((dado[:]))
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')