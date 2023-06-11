from unidecode import unidecode
nome = str(input('Qual é o seu nome? '))
nome = unidecode(nome)
nome = nome.strip().lower().capitalize()
if nome == 'Vinicius' or nome == 'Goi':
    print('Que nome lindo!')
elif nome == 'Michele' or nome == 'Miguel':
    print('Que nome bonito!')
elif nome in 'Igor, Here, Barone, Mayara':
    print('Você deve se orgulhar desse nome!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia,{}!'.format(nome))