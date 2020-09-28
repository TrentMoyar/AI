import random
import time
import sys
import multiprocessing

class Strategy():
   # implement all the required methods on your own
   def __init__(self):
      self.white = "o"
      self.black = "@"
      self.directions = None
      self.opposite_player = {self.black: self.white, self.white: self.black}
   def best_strategy(self, board, player, best_move, running):
      length = int(len(board)**0.5)
      self.directions = [length, length + 1, length - 1, -length, -length + 1, -length -1, -1, 1]
      moves = self.legal_moves(board,player)
      best = ((None,None), -1000000)
      for move in moves:
         m, v = move, self.minimax(self.make_move(board,player,move,moves[move]),player,0,-1, running)
         if v > best[1]:
            best = (m,v)
      best_move.value = best[0]
   def make_move(self, board, player, move, flipped):
      # returns board that has been updated
      board = list(board)
      board[move] = player
      for group in flipped:
         board[group] = player
      return board
   def minimax(self, board, player, search_depth, turn, running):
      moves = self.legal_moves(board,player if turn > 0 else self.opposite_player[player])
      if search_depth >= 3 or not running.value:
         return self.utility(board,player)
      best = None, -100000*turn
      for move in moves:
         m, v = move, self.minimax(self.make_move(board,player if turn > 0 else self.opposite_player[player],move,moves[move]),player,search_depth + 1,turn*-1, running)
         if v*turn > best[1]*turn:
            best = (m,v)
      return best[1]
   
   def utility(self, board, player):
      # returns the utility value
      this = 0
      opp = 0
      for pos in range(len(board)):
         if board[pos] == player:
            this += 1
         elif board[pos] == ('@' if player == 'o' else 'o'):
            opp += 1
      return this - opp
   def legal_moves(self, board, player):
      moves_found = {}
      for pos in range(len(board)):
            flipped_stones = self.find_flipped(board, pos, player)
            if len(flipped_stones) > 0:
               moves_found[pos] = flipped_stones
      return moves_found
   def find_flipped(self, board, position, player):
      length = int(len(board)**0.5)
      # finds which chips would be flipped given a move and player
      if board[position] != ".":
        return []
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         pos = position + incr
         while board[pos] != '?':
               if board[pos] == ".":
                  break
               if board[pos] == player:
                  flipped_stones += temp_flip
                  break
               temp_flip.append(pos)
               pos += incr
      return flipped_stones

def update_board(board, position, player):
   lboard = list(board)
   for flipped in find_flipped(board,position,player):
      lboard[flipped] = player
   lboard[position] = player
   return "".join(lboard)

def find_flipped(board, position, player):
      length = int(len(board)**0.5)
      directions = [length, length + 1, length - 1, -length, -length + 1, -length -1, -1, 1]
      # finds which chips would be flipped given a move and player
      if board[position] != ".":
        return []
      flipped_stones = []
      for incr in directions:
         temp_flip = []
         pos = position + incr
         while board[pos] != '?':
               if board[pos] == ".":
                  break
               if board[pos] == player:
                  flipped_stones += temp_flip
                  break
               temp_flip.append(pos)
               pos += incr
      return flipped_stones

def main():
   TIME = 3
   board = sys.argv[1]
   player = sys.argv[2]
   if player == "white":
      player = "o"
   else:
      player = "@"
   best_move = multiprocessing.Value('i')
   best_move.value = -1
   running = multiprocessing.Value('i')
   running.value = 1
   
   strategy = Strategy()
   p = multiprocessing.Process(target=strategy.best_strategy, args=(board, player, best_move, running))
   p.start()
   time.sleep(TIME - 0.005)
   running.value = 0
   time.sleep(0.005)
   p.join()
   if best_move.value != -1:
      board = update_board(board,best_move.value,player)
   print(board)




if __name__ =='__main__':
   main()