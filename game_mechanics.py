'''
A module containing Game_Mechanics class that is responsible
for handling game logic.
'''
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
        print(symbol)
        for i in range(Board.get_board_size()):
            self.line = 0
            for j in range(Board.get_board_size()):
                if (self.signs[i][j] == symbol):
                    self.line += 1
                    print(self.line)
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
        print(symbol)
        for j in range(Board.get_board_size()):
            self.line = 0
            for i in range(Board.get_board_size()):
                if (self.signs[i][j] == symbol):
                    self.line += 1
                    print(self.line)
                elif(self.signs[i][j] != symbol):
                    self.line = 0
                elif (self.line == 0) and ((Board.get_board_size() - i) < Board.get_row_win()):
                    break
                if (self.line >= Board.get_row_win()):
                    print("Wins!: "+symbol)
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

    def check_win(self, symbol: str):
        '''
        Checks if there is a winner on the current board
        '''
        result = self.check_horizontal(symbol) or self.check_vertical(symbol) or self.check_diagonal(symbol)
        print(result)
        if result:
            print(symbol + " WINS!")

        return result


class GameMechanics(HandleWin):
    '''
    Class responsible for handling game mechanics (mainly the minimax algorithm)
    '''

    def __init__(self, board_size):
        self.signs = [['-' for j in range(0, board_size)]
                      for i in range(0, board_size)]
        super().__init__(self.signs)

    def minimax(self):
        '''
        Minimax algorithm (recursive), returns the best score from a given
        recursion depth
        '''
        pass

    def best_move(self):
        '''
        This function calls minimax (which then calls itself recursivley) and returns the best
        move that the AI should pick
        '''
        # Will hold [x, y]
        # new_best_move = []
        # for each move in board :
        # for y in range(Board.decrement_board_size()):
        #     for x in range(Board.get_board_size()):
        #     if current move is better than bestMove
        #     bestMove = current move
        # Returns the best move
        pass


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

function bestMove() 
{
  // AI to make its turn
  let bestScore = -Infinity;
  let move;
  for (let i = 0; i < Board.get_board_size(); i++) 
  {
    for (let j = 0; j < Board.get_board_size(); j++) 
    {
      // Is the spot available?
      if (board[i][j] == '-') 
      {
        board[i][j] = 'o';
        let score = minimax(board, 0, false);
        board[i][j] = '-';
        if (score > bestScore) 
        {
          bestScore = score;
          move = 
          { i, j };
        }
      }
    }
  }
  board[move.i][move.j] = 'o';
  currentPlayer = human;
}

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
    for (let i = 0; i < 3; i++) 
    {
      for (let j = 0; j < 3; j++) 
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
