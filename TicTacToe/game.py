"""
Tic Tac Toe class + game play implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/ycubed
Github: https://www.github.com/kying18
"""

import time
import math
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_index = math.floor(square / 3)
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_index = square % 3
        col = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]

            if all([spot == letter for spot in diagonal_1]):
                return True

            if all([spot == letter for spot in diagonal_2]):
                return True

        return False

    def empty_squares(self):
        return ' ' in self.board  # returns a boolean

    def numbers_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_numbers()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to {}.'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)

    if print_game:
        print('It\'s a tie.')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    tic_tac_toe = TicTacToe()  # instance
    play(tic_tac_toe, x_player, o_player, print_game=True)
