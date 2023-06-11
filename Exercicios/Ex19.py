import random
pa = input('Digite o nome do primeiro aluno(a): ')
sa = input('Digite o nome do segundo aluno(a): ')
ta = input('Digite o nome do terceiro aluno(a): ')
qa = input('Digite o nome do quarto aluno(a): ')
l = [pa, sa, ta, qa]
print('O aluno(a) escolhido(a) foi {}'.format(random.choice(l)))