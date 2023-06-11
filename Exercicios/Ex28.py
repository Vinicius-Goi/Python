'''
Minha resolução:
import random
gen = random.randrange(0, 5)
p = int(input('Estou pensando em um número de 0 até 5, adivinhe-o: '))
if p == gen:
    print('Parabéns!Você adivinhou o número!')
else:
    print('Infelizmente você errou, a resposta era {}'.format(gen))
print('Obrigado pela sua participação :)')
'''
#Resolução do Guanabara
from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador sortear o num
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'* 20)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS!Você conseguiu me vencer!')
else:
    print('GANHEI! EU pensei no número {} e não no {}!'.format(computador, jogador))