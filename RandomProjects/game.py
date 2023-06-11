import time
from player import JogadorHumano, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # vamos usar uma lista simples para simular um 3x3
        self.current_winner = None #acompanhar um vencedor

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + '| '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (numeros correspondentes as caixas
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def quadrados_vazios(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, quadrado, letter):
        # se movimento válido, então faça o movimento (atribua o quadrado à letra)
        # então retorne verdadeiro. se inválido, retorne falso
        if self.board[quadrado] == ' ':
            self.board[quadrado] = letter
            if self.winner(quadrado, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, quadrado, letter):
        # winner if 3 in a row anywhere. whe have to check all these!
        # first let`s check the row
        row_ind = quadrado // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = quadrado % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        #but only if the squares is an even number (0,2,4,6,8)
        #these are the only moves possible to win a diagonal
        if quadrado % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        #if all of these fail
        return False

def play(game, x_player, o_player, print_game=True):
    #return the winner of the game(the letter)! or none for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # itera enquanto o jogo ainda tem quadrados vazios
    # (não precisamos nos preocupar com o vencedor porque apenas retornaremos isso
    # que quebra o loop)
    while game.quadrados_vazios():
        #conseguindo a jogada para o jogador certo
        if letter == 'O':
            quadrado = o_player.get_move(game)
        else:
            quadrado = x_player.get_move(game)

        #let's define a function to make a move!
        if game.make_move(quadrado, letter):
            if print_game:
                print(letter + ',faça a jogada para o quadrado {}'.format(quadrado))
                game.print_board()
                print('') #apenas uma linha vazia

            if game.current_winner:
                if print_game:
                    print(letter + ' \033[4;32mGANHOU\033[m!!')
                return letter

            #after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' #switches players

        #tiny break to make things a little easier to read
        time.sleep(0.8)

    if print_game:
        print('\033[4;33mEMPATE\033[m!')

if __name__ == '__main__':
    x_player = JogadorHumano('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)