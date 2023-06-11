import random
palpites = 0
gen = random.randrange(0, 10)
p = int(input('Estou pensando em um número de 0 até 10, adivinhe-o: '))
palpites += 1
if p == gen:
    print('Parabéns! Você adivinhou o número com {} palpite(s)!'.format(palpites))
while p != gen:
    palpites += 1
    p = int(input('Que pena, você errou! Mas não desista, tente novamente: '))
    if p == gen:
        print('Parabéns! Você adivinhou o número com {} palpite(s)!'.format(palpites))