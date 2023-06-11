f = str(input('Digite uma frase:  ')).lower().strip()
print('Na sua frase, aparece {} letras A'.format(f.count('a')))
print('A primeira letra A aparece na posição: {}'.format(f.find('a')+1))
print('A ultima letra A aparece na posição: {}'.format(f.rfind('a')+1))

