#- Listas []
'''dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) #Pedro
print(dados[1]) #25'''
#- Dicionarios {} APPEND NÃO FUNCIONA AQUI
'''dados = {'nome':"Pedro",'idade':25} #dict()
print(dados['nome']) #Pedro
print(dados['idade']) #Idade
dados['sexo'] = 'M' #add o indice 'sexo' na lista dados
#del dados['idade'] #eliminando o indice idade
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
        }
print(filme.values())#pegando todos os elementos do dicionario
print(filme.keys())#pegando os indices do dicionario
print(filme.items())#pegando tudo do dicionario
print('-='*30)
for k, v in filme.items():
    print(f'O {k} é {v}')'''

'''locadora = list()
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
        }
filme2 = {'titulo':'Avengers',
         'ano':2012,
         'diretor':'Joss Whedon'
        }
filme3 = {'titulo':'Matrix',
         'ano':1999,
         'diretor':'Machowski'
        }
locadora.append(filme)
locadora.append(filme2)
locadora.append(filme3)
print(locadora[0]['ano'])#1977
print(locadora[2]['titulo'])#matrix
'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['sexo']
#pessoas['nome'] = 'Goi'
'''pessoas['peso'] = 88.5
for k, v in pessoas.items():
    #print(k) keys
    #print(k) values
    print(f'{k} = {v}')'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
#print(estado1)
#print(estado2)

#print(brasil[0]['uf]) #Rio de Janeiro
print(brasil[1]['sigla'])#SP'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy()) #copiando o conteudo do dicionario para a lista
for e in brasil:
    #print(e)
    for k, v in e.items():
        #print(f'O campo {k} tem valor {v}')
        print(v, end=' ')
    print()