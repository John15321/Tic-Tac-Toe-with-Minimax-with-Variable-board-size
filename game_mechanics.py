"""A module containing Game_Mechanics class that is responsible for handling game logic."""
import pygame
from board_elements import *


class HandleWin():
    """
    A simple class that chekcs is there is a winner on the current board
    """

    def __init__(self, table):

        self.signs = [['-' for j in range(0, Board.get_board_size())]
                      for i in range(0, Board.get_board_size())]
        self.signs = table

    def check_horizontal(self, symbol):
        """
        Checks the horizontal axis to see if there is a winner
        """
        for i in range(Board.get_board_size()):
            self.line = 0
            for j in range(Board.get_board_size()):
                if self.signs[i][j] == symbol:
                    self.line += 1
                elif self.signs[i][j] != symbol:
                    self.line = 0
                elif self.line == 0 and ((Board.get_board_size() - j) < Board.get_row_win()):
                    break
                if self.line >= Board.get_row_win():
                    return True

    def check_vertical(self, symbol):
        """
        Checks the vertical axis to see if there is a winner
        """
        for j in range(Board.get_board_size()):
            self.line = 0
            for i in range(Board.get_board_size()):
                if self.signs[i][j] == symbol:
                    self.line += 1
                elif self.signs[i][j] != symbol:
                    self.line = 0
                elif (self.line == 0) and ((Board.get_board_size() - i) < Board.get_row_win()):
                    break
                if self.line >= Board.get_row_win():
                    return True

    def check_diagonal(self, symbol):
        """
        Checks the diagonal axis to see if there is a winner
        """
        win = []
        for i in range(Board.get_row_win()):
            win.append(symbol)

        for i in range(Board.get_board_size() - Board.get_row_win() + 1):

            diagonal = []
            x = i
            y = 0
            for j in range(Board.get_board_size() - i):
                diagonal.append(self.signs[x][y])
                x += 1
                y += 1
            for j in range(len(diagonal) - len(win) + 1):
                if win == diagonal[j:j + Board.get_row_win()]:
                    return True

            diagonal = []
            x = 0
            y = i
            for j in range(Board.get_board_size() - i):
                diagonal.append(self.signs[x][y])
                x += 1
                y += 1
            for j in range(len(diagonal) - len(win) + 1):
                if win == diagonal[j:j + Board.get_row_win()]:
                    return True

            diagonal = []
            x = Board.get_board_size() - 1 - i
            y = 0
            for j in range(Board.get_board_size() - i):
                diagonal.append(self.signs[x][y])
                x -= 1
                y += 1
            for j in range(len(diagonal) - len(win) + 1):
                if win == diagonal[j:j + Board.get_row_win()]:
                    return True

            diagonal = []
            x = Board.get_board_size() - 1
            y = 0 + i
            for j in range(Board.get_board_size() - i):
                diagonal.append(self.signs[x][y])
                x -= 1
                y += 1
            for j in range(len(diagonal) - len(win) + 1):
                if win == diagonal[j:j + Board.get_row_win()]:
                    return True

    def check_if_game_finish(self):
        """
        Simple function for checking if all places on the board are occupaied
        Returns True or False
        """
        for y in range(0, Board.get_board_size()):
            for x in range(0, Board.get_board_size()):
                if self.signs[y][x] == '-':
                    return False
        return True

    def check_win(self, symbol: str):
        """
        Checks if there is a winner on the current board
        """
        result = self.check_horizontal(symbol) or self.check_vertical(
            symbol) or self.check_diagonal(symbol)

        return result

    def who_won(self):
        """
        Returns who won the game
        """
        if self.check_win('x'):
            return 'x'
        elif self.check_win('o'):
            return 'o'
        elif self.check_if_game_finish() and (self.check_win('x') == False) and (self.check_win('o') == False):
            return 't'

    def calculate_score(self):
        """
        Calcualtes score
        """
        size = Board.get_board_size()
        score = 0
        for i in range(size):
            temp = 0
            for j in range(size):
                if self.signs[i][j] == 'o':
                    temp += 1
                elif self.signs[i][j] == '-':
                    temp = 0
                    break
            if temp != 0:
                score += 10**temp

        for i in range(size):
            temp = 0
            for j in range(size):
                if self.signs[j][i] == 'o':
                    temp += 1
                elif self.signs[j][i] == '-':
                    temp = 0
                    break
            if temp != 0:
                score += 10**temp

        temp = 0

        for i in range(size):
            if self.signs[i][i] == 'o':
                temp += 1
            elif self.signs[i][i] != '-':
                temp = 0
                break

        if temp != 0:
            score += 10**temp

        temp = 0

        for i in range(1, size):
            if self.signs[size - i][i - 1] == 'o':
                temp += 1
            if self.signs[size - i][i - 1] != 'o' and self.signs[size - 1][i - 1] != '-':
                temp = 0
                break

        if temp != 0:
            score += 10 ** temp
        return score


class GameMechanics(HandleWin):
    """
    Class responsible for handling game mechanics (mainly the minimax algorithm)
    """

    def __init__(self, board_size):
        self.signs = [['-' for j in range(0, board_size)]
                      for i in range(0, board_size)]
        super().__init__(self.signs)
        self.inf = 900000000
        self.max_depth = 5  # maximum recusion depth level, balances efficiency and AI predictions

    def Minimax(self, symbol, depth, a, b):
        """
        The main Minimax algorithm
        """
        if self.check_win(symbol):
            if symbol == 'o':
                return 10**8
            else:
                return -(10**8)

        if self.check_if_game_finish() or depth == 0:
            if symbol == 'o':
                return self.calculate_score()
            else:
                return (-1)*self.calculate_score()

        if symbol == 'x':
            symbol = 'o'
            best_score = (-1)*self.inf
        else:
            symbol = 'x'
            best_score = self.inf

        for i in range(Board.get_board_size()):
            for j in range(Board.get_board_size()):
                if self.signs[i][j] == '-':
                    if symbol == 'o':
                        self.signs[i][j] = symbol
                        m = self.Minimax(symbol, depth - 1, a, b)
                        if best_score < m:
                            best_score = m
                        if a < best_score:
                            a = best_score
                        self.signs[i][j] = '-'
                        if a >= b:
                            return best_score

                    else:
                        self.signs[i][j] = symbol
                        m = self.Minimax(symbol, depth - 1, a, b)
                        if best_score > m:
                            best_score = m
                        if b > best_score:
                            b = best_score
                        self.signs[i][j] = '-'
                        if a >= b:
                            return best_score

        return best_score

    def best_move(self):
        """
        Returns the best move that the AI should take!
        """
        best_score = (-1)*self.inf
        for i in range(Board.get_board_size()):
            for j in range(Board.get_board_size()):
                if self.signs[i][j] == '-':
                    self.signs[i][j] = 'o'
                    m = self.Minimax('o', self.max_depth, (-1) * self.inf, self.inf)
                    self.signs[i][j] = '-'
                    if m > best_score:
                        best_score = m
                        mov_i = i
                        mov_j = j

        self.signs[mov_i][mov_j] = 'o'
