import random
class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      # returns best move
      return best_move, 0

   def minimax(self, board, color, search_depth):
      # returns best "value"
      return 1

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_key(self, board, color):
      # hashes the board
      return 1

   def stones_left(self, board):
      # returns number of stones that can still be placed
      return 1

   def make_move(self, board, color, move, flipped):
      # returns board that has been updated
      return 1

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      return 1

   def score(self, board, color):
      # returns the score of the board 
      return 1

   def find_moves(self, board, color):
      # finds all possible moves
      return 1

   def find_flipped(self, board, x, y, color):
      # finds which chips would be flipped given a move and color
      return 1
class RandomBot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      if self.x_max == None:
         self.x_max = len(board)
      if self.y_max == None:
         self.y_max = len(board[0])
      # returns best move
      moves = self.find_moves(board,color)
      chosen = random.choice(list(moves.keys()))
      return chosen , 0

   def make_key(self, board, color):
      # hashes the board
      return 1

   def stones_left(self, board):
      # returns number of stones that can still be placed
      sum = 0
      for y in range(self.r_max):
         for x in range(self.c_max):
            if board[x][y] == '.':
               sum += 1
      return sum

   def find_moves(self, board, color):
      # finds all possible moves
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
               flipped_stones = self.find_flipped(board, i, j, color)
               if len(flipped_stones) > 0:
                  moves_found.update({(i,j): flipped_stones})
      return moves_found

   def find_flipped(self, board, x, y, color):
      # finds which chips would be flipped given a move and color
      if board[x][y] != ".":
        return []
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
               if board[x_pos][y_pos] == ".":
                  break
               if board[x_pos][y_pos] == color:
                  flipped_stones += temp_flip
                  break
               temp_flip.append([x_pos, y_pos])
               x_pos += incr[0]
               y_pos += incr[1]
      return flipped_stones

class Minimax_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      if self.x_max == None:
         self.x_max = len(board)
      if self.y_max == None:
         self.y_max = len(board[0])
      # returns best move
      moves = self.find_moves(board,color)
      best = ((None,None), -1000000)
      for move in moves:
         m, v = move, self.minimax(self.make_move(board,color,move,moves[move]),color,0,-1)
         if v > best[1]:
            best = (m,v)
      return best

   def minimax(self, board, color, search_depth, turn):
      # returns best "value"
      moves = self.find_moves(board,color if turn > 0 else self.opposite_color[color])
      if search_depth >= 3:
         return self.evaluate(board,color,None)
      best = None, -100000*turn
      for move in moves:
         m, v = move, self.minimax(self.make_move(board,color if turn > 0 else self.opposite_color[color],move,moves[move]),color,search_depth + 1,turn*-1)
         if v*turn > best[1]*turn:
            best = (m,v)
      return best[1]

   def make_move(self, board, color, move, flipped):
      # returns board that has been updated
      board = [x[:] for x in board]
      board[move[0]][move[1]] = color
      for group in flipped:
         board[group[0]][group[1]] = color
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      this = 0
      opp = 0
      for x in range(self.x_max):
         for y in range(self.y_max):
            if board[x][y] == color:
               this += 1
            elif board[x][y] == self.opposite_color[color]:
               opp += 1
      return this - opp

   def stones_left(self, board):
      # returns number of stones that can still be placed
      sum = 0
      for y in range(self.r_max):
         for x in range(self.c_max):
            if board[x][y] == '.':
               sum += 1
      return sum

   def find_moves(self, board, color):
      # finds all possible moves
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
               flipped_stones = self.find_flipped(board, i, j, color)
               if len(flipped_stones) > 0:
                  moves_found.update({(i,j): flipped_stones})
      return moves_found

   def find_flipped(self, board, x, y, color):
      # finds which chips would be flipped given a move and color
      if board[x][y] != ".":
        return []
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
               if board[x_pos][y_pos] == ".":
                  break
               if board[x_pos][y_pos] == color:
                  flipped_stones += temp_flip
                  break
               temp_flip.append([x_pos, y_pos])
               x_pos += incr[0]
               y_pos += incr[1]
      return flipped_stones
