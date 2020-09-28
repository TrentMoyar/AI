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
      self.c_x = None
      self.c_y = None
      self.values = None
      self.first_turn = True

   #board is a matrix
   def best_strategy(self, board, color):
      if color != "O" and color != "X":
         color = self.white if color == "#ffffff" else self.black
      self.x_max = len(board)
      self.y_max = len(board[0])
      self.c_x = len(board)//2
      self.c_y = len(board[0])//2
      self.values = {(x,y):set() for x in range(self.x_max) for y in range(self.y_max)}
      moves = self.find_moves(board, color)
      maxmove = max(moves,key=lambda move:self.alphabeta(self.make_move(board,color,move),color,0,-self.x_max**3,self.x_max**3))
      # returns best move
      #best_move is a tuple with: x_pos, y_pos
      return maxmove, 0

   def minimax(self, board, color, search_depth):
      # returns best "value"
      return 1

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
   def dist_from_cent(self,board,color):
      my_pos = None
      op_pos = None
      for val in self.values:
         if board[val[0]][val[1]] == color:
            my_pos = val
         if board[val[0]][val[1]] == self.opposite_color[color]:
            op_pos = val
      return (my_pos[0]-self.c_x)**2+(my_pos[1]-self.c_y)**2

   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      moves = self.find_moves(board,color)
      if search_depth == 5 or len(moves) == 0:
         opmoves = self.find_moves(board,self.opposite_color[color])
         if len(moves) > 0:
            return self.dist_from_cent(board,self.opposite_color[color])*len(moves)**2-self.dist_from_cent(board,color)*len(opmoves)**2
         return 0
      #tuples = [(x,self.alphabeta(self.make_move(board,color,x),color,search_depth + 1,-self.x_max**3,self.x_max**3)) for x in moves]
      if search_depth%2 == 1:
         value = -100000
         for x in moves:
            value = max(value, self.alphabeta(self.make_move(board,color,x),color,search_depth + 1,alpha,beta))
            alpha = max(alpha, value)
            if alpha >= beta:
               break
         return value
      else:
         value = 100000
         for x in moves:
            value = min(value, self.alphabeta(self.make_move(board,color,x),color,search_depth + 1,alpha,beta))
            beta = min(beta, value)
            if alpha >= beta:
               break
         return value


   def make_move(self, board, color, move):
      # returns board that has been updated
      board = [x[:] for x in board]
      for val in self.values:
         if board[val[0]][val[1]] == color:
            board[val[0]][val[1]] = 'W'
      board[move[0]][move[1]] = color
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      return len(self.find_moves(board,color))

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
