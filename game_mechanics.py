'''
A module containing Game_Mechanics class that is responsible
for handling game logic.
'''
import pygame
from board_elements import *


class HandleWin():
    '''
    A simple class that chekcs is there is a winner on the current board
    '''

    def __init__(self, table):

        self.signs = [['-' for j in range(0, Board.get_board_size())]
                      for i in range(0, Board.get_board_size())]
        self.signs = table

    def check_horizontal(self, symbol):
        '''
        Checks the horizontal axis to see if there is a winner
        '''
        for i in range(Board.get_board_size()):
            self.line = 0
            for j in range(Board.get_board_size()):
                if (self.signs[i][j] == symbol):
                    self.line += 1
                elif(self.signs[i][j] != symbol):
                    self.line = 0
                elif self.line == 0 and ((Board.get_board_size() - j) < Board.get_row_win()):
                    break
                if (self.line >= Board.get_row_win()):
                    return True

    def check_vertical(self, symbol):
        '''
        Checks the vertical axis to see if there is a winner
        '''
        for j in range(Board.get_board_size()):
            self.line = 0
            for i in range(Board.get_board_size()):
                if (self.signs[i][j] == symbol):
                    self.line += 1
                elif(self.signs[i][j] != symbol):
                    self.line = 0
                elif (self.line == 0) and ((Board.get_board_size() - i) < Board.get_row_win()):
                    break
                if (self.line >= Board.get_row_win()):
                    return True

    def check_diagonal(self, symbol):
        '''
        Checks the diagonal axis to see if there is a winner
        '''
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
        '''
        Simple function for checking if all places on the board are occupaied
        Returns True or False
        '''
        covered = 0
        for y in range(0, Board.get_board_size()):
            for x in range(0, Board.get_board_size()):
                if self.signs[y][x] != '-':
                    covered += 1
        return covered == Board.get_board_size()**2

    def check_win(self, symbol: str):
        '''
        Checks if there is a winner on the current board
        '''
        result = self.check_horizontal(symbol) or self.check_vertical(
            symbol) or self.check_diagonal(symbol)

        return result

    def who_won(self):
        if self.check_win('x'):
            return 'x'
        elif self.check_win('o'):
            return 'o'
        elif self.check_if_game_finish() and (self.check_win('x')==False) and (self.check_win('o')==False):
            return 't'


class GameMechanics(HandleWin):
    '''
    Class responsible for handling game mechanics (mainly the minimax algorithm)
    '''

    def __init__(self, board_size):
        self.signs = [['-' for j in range(0, board_size)]
                      for i in range(0, board_size)]
        super().__init__(self.signs)

    def minimax(self, is_maximizing):
        '''
        Minimax algorithm (recursive), returns the best score from a given
        recursion depth
        '''
        result = self.who_won()
        if (result == 'x'):
            return -1
        elif result == 'o':
            return 1
        elif result == 't':
            return 0

        if (is_maximizing):
            best_score = -99999999
            for i in range(0, Board.get_board_size()):
                for j in range(0, Board.get_board_size()):
                    if self.signs[i][j] == '-':
                        self.signs[i][j] = 'o'
                        score = self.minimax(False)
                        self.signs[i][j] = '-'
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 99999999
            for i in range(0, Board.get_board_size()):
                for j in range(0, Board.get_board_size()):
                    if self.signs[i][j] == '-':
                        self.signs[i][j] = 'x'
                        score = self.minimax(True)
                        self.signs[i][j] = '-'
                        best_score = min(score, best_score)
            return best_score


    def best_move(self):
        '''
        This function calls minimax (which then calls itself recursivley) and returns the best
        move that the AI should pick
        '''
        best_score = -99999999
        # Will hold [x, y]
        new_best_move = [0,0]
        # for each move in board:
        for y in range(0, Board.get_board_size()):
            for x in range(0, Board.get_board_size()):
                if self.signs[y][x] == '-':
                    self.signs[y][x] = 'o'
                    score = self.minimax(False)
                    self.signs[y][x] = '-'
                    if score > best_score:
                        best_score = score
                        new_best_move = [y, x]

        if self.signs[new_best_move[0]][new_best_move[1]] == '-':
            self.signs[new_best_move[0]][new_best_move[1]] = 'o'

        #     if current move is better than bestMove
        #     bestMove = current move
        # Returns the best move


'''
TODO:
1. Przekazywac Game_Mechanics stan gry i go ogolnie updatowac
2. Na postawie Game_Mechanics(minimax) zrobic prediction gdzie ma byc ruch O
3. O musi zrobic swoj ruch
4. Aktualizacja planszy
5. Patrzymy czy jest wygrana
6. Graczc robi ruch i sie powtarza
'''


'''

let scores = 
{
  X: 10,
  O: -10,
  tie: 0
};

function minimax(board, depth, isMaximizing) 
{
  let result = checkWinner();
  if (result !== null) 
  {
    return scores[result];
  }

  if (isMaximizing) 
  {
    let bestScore = -Infinity;
    for (let i = 0; i < Board.get_board_size(); i++) 
    {
      for (let j = 0; j < Board.get_board_size(); j++) 
      {
        // Is the spot available?
        if (board[i][j] == '') 
        {
          board[i][j] = ai;
          let score = minimax(board, depth + 1, false);
          board[i][j] = '';
          bestScore = max(score, bestScore);
        }
      }
    }
    return bestScore;
  } else 
  {
    let bestScore = Infinity;
    for (let i = 0; i < Board.get_board_size(); i++) 
    {
      for (let j = 0; j < Board.get_board_size(); j++) 
      {
        // Is the spot available?
        if (board[i][j] == '') 
        {
          board[i][j] = human;
          let score = minimax(board, depth + 1, true);
          board[i][j] = '';
          bestScore = min(score, bestScore);
        }
      }
    }
    return bestScore;
  }
}

'''
