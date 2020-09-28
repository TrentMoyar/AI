#Trent Moyar
#Period 3
import math
def is_not_valid(board_poss, col, col_indices, N):
   for x in range(col,N):
      no = 0
      for y in col_indices[x]:
         no += board_poss[y]
      if no == 0:
         return True
   return False

def recur_solve(added,board_vals, board_poss, NEIGHBORS, col_indices, N, col):
   if added != None:
      board_vals[added] = 1
      for x in NEIGHBORS[added]:
         board_poss[x] = 0
   if is_not_valid(board_poss, col, col_indices, N):
      return None
   if col == N:
      return board_vals
   vars = select_vars(board_poss, NEIGHBORS, col_indices[col], N)
   for x in vars:
      result = recur_solve(x,board_vals[:],board_poss[:], NEIGHBORS, col_indices, N, col + 1)
      if result != None:
         return result
   return None

def select_vars(board_poss, NEIGHBORS, col_indices, N):
   poss = [x for x in col_indices if board_poss[x] == 1]
   return sorted(poss, key = lambda yeet: find_affected(yeet,board_poss,NEIGHBORS))
def find_affected(index, board_poss, NEIGHBORS):
   sum = 0
   for x in NEIGHBORS[index]:
      sum += board_poss[x]
   return sum
def get_col_indices(N, board_poss):
   toreturn = {}
   for col in range(N):
      toreturn[col] = [col + x*N for x in range(N) if board_poss[col + x*N] == 1]
   return toreturn
def main():
   N = int(input("What is N? "))
   for x in range(4,N):
      NEIGHBORS = create_neighbors(x)
      board_poss = [1 for y in range(x*x)]
      board_vals = [0 for y in range(x*x)]
      print(x)
      display(recur_solve(None, board_vals[:], board_poss[:], NEIGHBORS, get_col_indices(x, board_poss), x, 0), x)

def create_neighbors(N):
   NEIGHBORS = [set() for x in range(N*N)]
   for index in range(N*N):
      index_col = index%N
      for x in range(N):
         NEIGHBORS[index].add(index_col + x*N)
      index_row = index//N
      for x in range(N):
         NEIGHBORS[index].add(index_row*N + x)

      index_col = index%N
      index_row = index//N
      while index_row < N and index_col < N:
         NEIGHBORS[index].add(index_row*N + index_col)
         index_row += 1
         index_col += 1
      index_col = index%N
      index_row = index//N
      while index_row < N and index_col >= 0:
         NEIGHBORS[index].add(index_row*N + index_col)
         index_row += 1
         index_col -= 1
      index_col = index%N
      index_row = index//N
      while index_row > 0 and index_col < N:
         NEIGHBORS[index].add(index_row*N + index_col)
         index_row -= 1
         index_col += 1
      index_col = index%N
      index_row = index//N
      while index_row >= 0 and index_col >= 0:
         NEIGHBORS[index].add(index_row*N + index_col)
         index_row -= 1
         index_col -= 1
   return NEIGHBORS
def display(board,N):
   for x in range(N):
      print(board[x*N:x*N+N])
if __name__ == '__main__':
   main()