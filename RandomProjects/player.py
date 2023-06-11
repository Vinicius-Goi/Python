import math
import random

class player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    #queremos fazer todos os jogadores jogarem
    def movimento(self, game):
        pass

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid spot for our next move
        quadrado = random.choice(game.available_moves())
        return quadrado

class JogadorHumano(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        quadrado_valido = False
        val = None
        while not quadrado_valido:
            quadrado = input(self.letter + ' é seu turno, entre com o seu movimento (0-8): ')
            # vamos verificar se este é um valor correto tentando converter
            # para um inteiro, e se não for, dizemos que é inválido
            # se esse ponto não estiver disponível no tabuleiro, também dizemos que é inválido
            try:
                val = int(quadrado)
                if val not in game.available_moves():
                    raise ValueError
                quadrado_valido = True #se forem bem sucedidos, então yay!
            except ValueError:
                print('Quadrado \033[4;31mINVÁLIDO\033[m!Tente novamente.')

        return val