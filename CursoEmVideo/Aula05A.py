'''Manipulação de Cadeia de Textos
Exemplo: Curso em Video Python - Para o python, isso é a string, q sempre está entre '' ou ""
'''
'''
#Fatiamento
frase = 'Curso em Video - Python'
print(frase)
print(frase[9]) #Usando o indice da variavel frase eu posso fatiar e apresentar somente uma casa que eu queira
print(frase[9:23]) #Usando o indice da variavel frase eu posso fatiar e apresentar pedaços que eu queira
print(frase[9:23:2]) #Usando o indice da variavel frase eu posso fatiar e apresentar pedaços que eu queira porem, pulando de 2 em 2 (que nesse caso é o número digitado)
print(frase[:5])#N colocando o numero inicial, ele irá começar pela primeira casa [0] até o numero escolhido [5], basicamente como se fosse o print(frase[0:5])
print(frase[15:])#N colocando o numero final, ele irá começar na casa digitada e cortar as anteriores, nesse caso, a casa digitada foi [15] então, ele irá cortar todas os indices atras dele
print(frase[9::3])#Desse jeito, ele irá começar no indice 9 e vai ir até o final, já que n foi especificado, porem pulando de 3 em 3 casas
print(frase[::3])#Pega toda a palavra, pulando 3 casas
'''
'''
#Análise
frase = 'Curso em Video - Python'
print(len(frase))#len mostra a quant de caracteres na string
print(frase.count('o'))#.count mostra a quant de caracteres desejados, nesse caso, o 'o', entretanto, ele n mostrará as letras maiusculas, somente se vc digitar 'O'
print(frase.count('o',0,13))#Assim ele mostrará a quant de 'o' no fatiamento desejado, ou seja do indice 0 até o 13 (embora a ultima casa digitada sempre será ignorada)
print(frase.find('deo'))#Aqui ele encontrará o momento em que deo se iniciou, ou seja, ele mostrará na casa 11
print(frase.find('Android'))#Se vc receber o valor -1 isso quer dizer, que n há nenhuma região onde tem a palavra 'Android'
print('Curso'in frase)#O operador 'in' vai me mostrar se existe tal palavra na frase, se tiver, é true, senão false
'''
'''
#Transformação
frase = 'Curso em Video - Python'
print(frase.replace('Python', 'Android'))#Aqui ele substituirá o termo 'Python' por 'Android'
print(frase.upper())#Upper deixará todas as casas com letras maiusculas
print(frase.lower())#Lower deixará todas as casas com letras minusculas
print(frase.capitalize())#Ele vai deixar somente a primeira casa com letra maiscula
print(frase.title())#Ele vai fazer o capitaliza, só q dessa vez, palavra por palavra
'''
'''
frase = '   Aprenda Python  '
print(frase)
print(frase.strip())#Remove todos os espaços inuteis no final e no inicio
print(frase.rstrip())#Remove todos os espaços inuteis no lado direito
print(frase.lstrip())#Remove todos os espaços inuteis no lado esquerdo
'''
'''
#Divisão
frase = 'Curso em Video - Python'
print(frase)
print(frase.split())#Ele vai marcar e dividir sua frase, considerando os espaços q há nela
'''
'''
#Junção
frase = 'Curso em Video - Python'
print(frase)
print('-'.join(frase))#A cada letra, ele irá juntar e colocar um '-' na frase
'''
#Print com um blocão de texto
#print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
#Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
#Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
#Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')
