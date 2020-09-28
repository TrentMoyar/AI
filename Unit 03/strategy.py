import random
import time
import sys
import multiprocessing



ONES = [1 << x for x in range(64)]
LENGTH = 8
SIZE = 64
PADSIZE = 100
MIN = -10000000
MAX = 10000000

CORNERS = int((
   "10000001"
   "00000000"
   "00000000"
   "00000000"
   "00000000"
   "00000000"
   "00000000"
   "10000001"), base=2)

EDGES = int((
   "01111110"
   "10000001"
   "10000001"
   "10000001"
   "10000001"
   "10000001"
   "10000001"
   "01111110"), base=2)

LEFT_MASK = int((
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"), base=2)
RIGHT_MASK = int((
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"), base=2)
UP_MASK = int((
   "11111111"
   "11111111"
   "11111111"
   "11111111"
   "11111111"
   "11111111"
   "11111111"
   "00000000"), base=2)
DOWN_MASK = int((
   "00000000"
   "11111111"
   "11111111"
   "11111111"
   "11111111"
   "11111111"
   "11111111"
   "11111111"), base=2)
UL_MASK = int((
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "00000000"), base=2)
UR_MASK = int((
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "00000000"), base=2)
DL_MASK = int((
   "00000000"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"
   "11111110"), base=2)
DR_MASK = int((
   "00000000"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"
   "01111111"), base=2)

CORNERS = int((
   "10000001"
   "00000000"
   "00000000"
   "00000000"
   "00000000"
   "00000000"
   "00000000"
   "10000001"), base=2)

FORDIAG = int((
   "00000001"
   "00000010"
   "00000100"
   "00001000"
   "00010000"
   "00100000"
   "01000000"
   "10000000"), base=2)

BACKDIAG = int((
   "10000000"
   "01000000"
   "00100000"
   "00010000"
   "00001000"
   "00000100"
   "00000010"
   "00000001"), base=2)


def shift_left(board):
   return (board << 1) & LEFT_MASK
def shift_right(board):
   return (board >> 1) & RIGHT_MASK
def shift_up(board):
   return (board << LENGTH) & UP_MASK
def shift_down(board):
   return (board >> LENGTH) & DOWN_MASK
def shift_upr(board):
   return (board << LENGTH - 1) & UR_MASK
def shift_upl(board):
   return (board << LENGTH + 1) & UL_MASK
def shift_downr(board):
   return (board >> LENGTH + 1) & DR_MASK
def shift_downl(board):
   return (board >> LENGTH - 1) & DL_MASK
shift_funcs = [shift_right, shift_left, shift_up, shift_down, shift_upr, shift_downl, shift_upl, shift_downr]
def multi_shift(board, times, func):
   for x in range(times):
      board = func(board)
   return board

UL_MATRIX = [multi_shift(FORDIAG,LENGTH - 1 - x,shift_left) for x in range(LENGTH - 1)] + [FORDIAG] + [multi_shift(FORDIAG,x + 1,shift_right) for x in range(LENGTH - 1)]
DR_MATRIX = [multi_shift(FORDIAG,LENGTH - 1 - x,shift_right) for x in range(LENGTH - 1)] + [FORDIAG] + [multi_shift(FORDIAG,x + 1,shift_left) for x in range(LENGTH - 1)]
DL_MATRIX = [multi_shift(BACKDIAG,LENGTH - 1 - x,shift_left) for x in range(LENGTH - 1)] + [BACKDIAG] + [multi_shift(BACKDIAG,x + 1,shift_right) for x in range(LENGTH - 1)]
UR_MATRIX = [multi_shift(BACKDIAG,LENGTH - 1 - x,shift_right) for x in range(LENGTH - 1)] + [BACKDIAG] + [multi_shift(BACKDIAG,x + 1,shift_left) for x in range(LENGTH - 1)]

DOWN_LINES = [sum([1 << x + y*LENGTH for x in range(LENGTH)]) for y in range(LENGTH)]
RIGHT_LINES = [sum([1 << x*LENGTH + y for x in range(LENGTH)]) for y in range(LENGTH)]
LEFT_LINES = RIGHT_LINES[::-1]
UP_LINES = DOWN_LINES[::-1]

def UL_STABILITY(board):
   toreturn = 0
   upindex = LENGTH
   leftindex = LENGTH
   diag = 1
   for x in UL_MATRIX:
      temp = x & board
      tempindex = 0
      for y in UP_LINES:
         if tempindex == upindex or tempindex == diag:
            break
         if (temp & y) == 0:
            upindex = tempindex
            break
         toreturn |= (temp & y)
         tempindex += 1
      tempindex = 0
      for y in LEFT_LINES:
         if tempindex == leftindex or tempindex == diag:
            break
         if (temp & y) == 0:
            leftindex = tempindex
            break
         toreturn |= (temp & y)
         tempindex += 1
      diag += 1
   return toreturn
         
def UR_STABILITY(board):
   toreturn = 0
   upindex = LENGTH
   rightindex = LENGTH
   diag = 1
   for x in UR_MATRIX:
      temp = x & board
      tempindex = 0
      for y in UP_LINES:
         if tempindex == upindex or tempindex == diag:
            break
         if (temp & y) == 0:
            upindex = tempindex
            break
         toreturn |= (temp & y)
         tempindex += 1
      tempindex = 0
      for y in RIGHT_LINES:
         if tempindex == rightindex or tempindex == diag:
            break
         if (temp & y) == 0:
            rightindex = tempindex
            break
         toreturn |= (temp & y)
         tempindex += 1
      diag += 1
   return toreturn

def DL_STABILITY(board):
   toreturn = 0
   downindex = LENGTH
   leftindex = LENGTH
   diag = 1
   for x in DL_MATRIX:
      temp = x & board
      tempindex = 0
      for y in DOWN_LINES:
         if tempindex == downindex or tempindex == diag:
            break
         if (temp & y) == 0:
            downindex = tempindex
            break
         toreturn |= (temp & y)
         tempindex += 1
      tempindex = 0
      for y in LEFT_LINES:
         if tempindex == leftindex or tempindex == diag:
            break
         if (temp & y) == 0:
            leftindex = tempindex
            break
         toreturn |= (temp & y)
         tempindex += 1
      diag += 1
   return toreturn

def DR_STABILITY(board):
   toreturn = 0
   downindex = LENGTH
   rightindex = LENGTH
   diag = 1
   for x in DR_MATRIX:
      temp = x & board
      tempindex = 0
      for y in DOWN_LINES:
         if tempindex == downindex or tempindex == diag:
            break
         if (temp & y) == 0:
            downindex = tempindex
            break
         toreturn |= (temp & y)
         tempindex += 1
      tempindex = 0
      for y in RIGHT_LINES:
         if tempindex == rightindex or tempindex == diag:
            break
         if (temp & y) == 0:
            rightindex = tempindex
            break
         toreturn |= (temp & y)
         tempindex += 1
      diag += 1
   return toreturn

def check_stability(board):
   return DR_STABILITY(board) | DL_STABILITY(board) | UL_STABILITY(board) | UR_STABILITY(board)

def legal_moves(myboard, opboard):
   toreturn = 0
   for func in shift_funcs:
      shifted = func(myboard)
      shifted &= opboard
      while shifted != 0:
         shifted = func(shifted)
         toreturn |= shifted & (~opboard) & (~myboard)
         shifted &= opboard
   return toreturn

def split_binary(binary):
   toreturn = []
   for x in ONES:
      x &= binary
      if x:
         toreturn.append(x)
   return toreturn

def flipped_stones(piece, myboard, opboard):
   toreturn = 0
   for func in shift_funcs:
      tmp = 0
      shifted = func(piece)
      while shifted & opboard:
         tmp |= shifted
         shifted = func(shifted)
      if shifted & myboard:
         toreturn |= tmp
   return toreturn

def make_move(myboard, opboard, piece, flipped):
   myboard |= piece
   myboard |= flipped
   opboard &= ~flipped

   return myboard, opboard

def my_moves(myboard,opboard):
   toreturn = []
   legals = split_binary(legal_moves(myboard, opboard))
   for move in legals:
      flipped = flipped_stones(move, myboard, opboard)
      toreturn.append(make_move(myboard, opboard, move, flipped))
   return toreturn

def op_moves(myboard,opboard):
   toreturn = []
   legals = split_binary(legal_moves(opboard, myboard))
   for move in legals:
      flipped = flipped_stones(move, opboard, myboard)
      board = make_move(opboard, myboard, move, flipped)
      toreturn.append((board[1],board[0]))
   return toreturn

def split_string(board, player):
   opponent = '@' if player == 'o' else 'o'
   myboard = 0
   opboard = 0
   played = 0
   index = 0
   for x in range(100-1,-1,-1):
      if board[x] != '?':
         if board[x] == player:
            myboard |= ONES[index]
         if board[x] == opponent:
            opboard |= ONES[index]
         index += 1
   return myboard, opboard

def get_move(piece):
   index = 0
   while piece:
      piece = piece >> 1
      index += 1
   index = SIZE - index
   row = index // 8
   index += (row)*2 + 11
   return index

def bit_count(binary):
   toreturn = 0
   for x in ONES:
      if x & binary:
         toreturn += 1
   return toreturn

class Strategy():
   # implement all the required methods on your own
   def best_strategy(self, board, player, best_move, running):
      myboard, opboard = split_string(board, player)
      depth = 1
      prevtable = {}
      if bit_count(myboard|opboard) >= 54:
         boards = self.alpha_beta(myboard, opboard, 64, MIN, MAX, prevtable)
         best_move.value = get_move((myboard | opboard) ^ (boards[0] | boards[1]))
      else:
         while running.value:
            boards = self.alpha_beta(myboard, opboard, depth, MIN, MAX, prevtable)
            best_move.value = get_move((myboard | opboard) ^ (boards[0] | boards[1]))
            depth += 1
   def get_weight(self, move, myboard, opboard, table):
      flipped = flipped_stones(move, myboard, opboard)
      numy, nuop = make_move(myboard, opboard, move, flipped)
      if (numy, nuop) in table:
         return table[(numy,nuop)]
      else:
         return 0
   def coin_heur(self,myboard,opboard):
      return 100*(bit_count(myboard)-bit_count(opboard))/(bit_count(myboard)+bit_count(opboard))
   def mobility_heur(self,myboard,opboard):
      mymoves = bit_count(legal_moves(myboard, opboard))
      opmoves = bit_count(legal_moves(opboard, myboard))
      if mymoves | opmoves:
         return 100*(mymoves - opmoves)/(mymoves + opmoves)
      return 0
   def corner_heur(self,myboard,opboard):
      mycornheur = bit_count(CORNERS & myboard) + bit_count(CORNERS & legal_moves(myboard,opboard))
      opcornheur = bit_count(CORNERS & opboard) + bit_count(CORNERS & legal_moves(opboard,myboard))
      if mycornheur | opcornheur:
         return 100*(mycornheur-opcornheur)/(mycornheur+opcornheur)
      return 0
   def stability_heur(self,myboard,opboard):
      mystability = bit_count(check_stability(myboard))
      opstability = bit_count(check_stability(opboard))
      if mystability | opstability:
         return 100*(mystability - opstability)/(mystability + opstability)
      return 0
   def evaluate(self, myboard, opboard):
      corners = self.corner_heur(myboard,opboard)
      mobility = self.mobility_heur(myboard,opboard)
      stability = self.stability_heur(myboard,opboard)
      return corners*0.3 + mobility*0.4 + stability*0.3
   def alpha_beta(self, myboard, opboard, depth, alpha, beta, prevtable):
      table = {}
      moves = my_moves(myboard,opboard)
      v = self.max_value(myboard, opboard, depth, MIN, MAX, table, prevtable)
      for move in moves:
         if move in table and table[move] == v:
            prevtable = table
            return move
      return -1
   def max_value(self, myboard, opboard, depth, alpha, beta, table, prevtable):
      mymoves = legal_moves(myboard, opboard)
      opmoves = legal_moves(opboard, myboard)
      if mymoves | opmoves == 0:
         return 1000*bit_count(myboard) if bit_count(myboard) > bit_count(opboard) else -1000*bit_count(opboard)
      elif mymoves == 0:
         return self.min_value(myboard,opboard,depth,alpha,beta, table, prevtable)
      if depth == 0:
         return self.evaluate(myboard, opboard)
      moves = my_moves(myboard, opboard)
      v = MIN
      for move in moves:
         m = None
         if move in table:
            m = table[move]
         else:
            m = self.min_value(move[0], move[1], depth - 1, alpha, beta, table, prevtable)
            table[move] = m
         v = v if v > m else m
         if v >= beta:
            return v
         alpha = alpha if alpha > v else v
      return v
   def min_value(self, myboard, opboard, depth, alpha, beta, table, prevtable):
      mymoves = legal_moves(myboard, opboard)
      opmoves = legal_moves(opboard, myboard)
      if mymoves | opmoves == 0:
         return 1000*bit_count(myboard) if bit_count(myboard) > bit_count(opboard) else -1000*bit_count(opboard)
      elif opmoves == 0:
         return self.max_value(myboard,opboard,depth,alpha,beta,table, prevtable)
      if depth == 0:
         return self.evaluate(myboard, opboard)
      moves = op_moves(myboard, opboard)
      v = MAX
      for move in moves:
         if move in table:
            m = table[move]
         else:
            m = self.max_value(move[0], move[1], depth - 1, alpha, beta, table, prevtable)
            table[move] = m
         v = v if v < m else m
         if v <= alpha:
            return v
         beta = beta if beta < v else v
      return v



