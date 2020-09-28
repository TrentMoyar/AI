# Name: Trent Moyar
import random

class RandomPlayer:
   def __init__(self):
      self.white = "O"
      self.black = "X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True
   
   #board is a matrix
   def best_strategy(self, board, rcolor):
      # returns best move
      color = self.white if rcolor == "#ffffff" else self.black
      self.x_max = len(board)
      self.y_max = len(board[0])
      moves = self.find_moves(board,color)
      #last value not used in end, as this method is recursive
      #best_move is a tuple with: x_pos, y_pos
      return random.choice(list(moves)), 0
      
   def make_move(self, board, color, move):
      # returns board that has been updated
      return board
   def find_moves(self, board, color):
      # finds all possible moves
      #x,y = [(x,y) for ix, x in enumerate(board) if for iy, y in enumerate(x) if y == color]
      my_pos = None
      op_pos = None
      values = {(x,y):set() for x in range(self.x_max) for y in range(self.y_max)}
      for val in values:
         if board[val[0]][val[1]] == color:
            my_pos = val
         if board[val[0]][val[1]] == self.opposite_color[color]:
            op_pos = val
      if my_pos == None:
         if op_pos == None:
            return values
         del values[op_pos]
         return values
      toreturn = set()
      for direc in self.directions:
         temp = (my_pos[0] + direc[0], my_pos[1] + direc[1])
         while temp[0] < self.x_max and temp[1] < self.y_max and temp[0] >= 0 and temp[1] >= 0 and board[temp[0]][temp[1]] == '.':
            toreturn.add(temp)
            temp = (temp[0] + direc[0], temp[1] + direc[1])
      return toreturn

class CustomPlayer:

   def __init__(self):
      self.white = "O"
      self.black = "X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True

   #board is a matrix
   def best_strategy(self, board, color):
      if color != "O" and color != "X":
         color = self.white if color == "#ffffff" else self.black
      self.x_max = len(board)
      self.y_max = len(board[0])
      moves = self.find_moves(board, color)
      moves = [self.make_move(board,color,x) for x in moves]
      maxmove = max(moves,key=lambda board:self.alphabeta(board,color,0))
      # returns best move
      #best_move is a tuple with: x_pos, y_pos
      return maxmove, 0

   def minimax(self, board, color, search_depth):
      # returns best "value"
      return 1

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      if search_depth == 3:
         return self.evaluate(board,color,None)
      pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      my_pos = None
      op_pos = None
      toreturn = 0
      for direc in self.directions:
         temp = (my_pos[0] + direc[0], my_pos[1] + direc[1])
         while temp[0] < self.x_max and temp[1] < self.y_max and temp[0] >= 0 and temp[1] >= 0 and board[temp[0]][temp[1]] == '.':
            toreturn += 1
            temp = (temp[0] + direc[0], temp[1] + direc[1])
      return toreturn

   def find_moves(self, board, color):
      # finds all possible moves
      #x,y = [(x,y) for ix, x in enumerate(board) if for iy, y in enumerate(x) if y == color]
      my_pos = None
      op_pos = None
      values = {(x,y):set() for x in range(self.x_max) for y in range(self.y_max)}
      for val in values:
         if board[val[0]][val[1]] == color:
            my_pos = val
         if board[val[0]][val[1]] == self.opposite_color[color]:
            op_pos = val
      if my_pos == None:
         if op_pos == None:
            return values
         del values[op_pos]
         return values
      toreturn = set()
      for direc in self.directions:
         temp = (my_pos[0] + direc[0], my_pos[1] + direc[1])
         while temp[0] < self.x_max and temp[1] < self.y_max and temp[0] >= 0 and temp[1] >= 0 and board[temp[0]][temp[1]] == '.':
            toreturn.add(temp)
            temp = (temp[0] + direc[0], temp[1] + direc[1])
      return toreturn
