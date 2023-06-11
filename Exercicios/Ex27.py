nome = input('Digite seu nome completo: ').strip()
n = nome.split()
print('Olá {}! Prazer em te conhecer!\nSeu primeiro nome é {}'.format(nome, n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))