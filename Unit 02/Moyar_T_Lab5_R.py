#Trent Moyar
#Period 3
import math, random

heur_dict = {}
def heuristic(board, N):
   global heur_dict
   represent = tuple(board)
   if represent in heur_dict:
      return heur_dict[represent]
   diag1 = [0 for x in range(N*2 - 1)]
   diag2 = [0 for x in range(N*2 - 1)]
   rows = [0 for x in range(N)]
   cols = [0 for x in range(N)]
   sum = 0
   for x in range(N):
      ri = board[x]
      ci = x
      sum += cols[ci]
      cols[ci] += 1
      sum += rows[ri]
      rows[ri] += 1
      sum += diag1[ri + ci]
      diag1[ri + ci] += 1
      sum += diag2[ri - ci + (N - 1)]
      diag2[ri - ci + (N - 1)] += 1
   heur_dict[represent] = sum
   return sum
def random_board(N):
   return [random.randrange(0,N) for x in range(N)]
def solve(N):
   board = random_board(N)
   #neighbors = create_neighbors(N)
   print(get_adjs(board,N))
   print(heuristic(board, N))
   heur = heuristic(board, N)
   while True:
      if heur == 0:
         return board
      adjs = get_adjs(board, N)
      best = find_best(adjs, N)
      hb = heuristic(best, N)
      if hb < heur:
         heur = hb
         board = best
      else:
         board = random_board(N)
         heur = heuristic(board,N)
   return None
      
   
def find_best(adjs, N):
   min = N*N*N
   pos = 0
   for x in range(len(adjs)):
      heur = heuristic(adjs[x],N)
      if heur < min:
         pos = x
         min = heur
   return adjs[pos]


def get_adjs(board, N):
   to_return = []
   for col in range(N):
      for value in range(N):
         if value != board[col]:
            temp = board[:]
            temp[col] = value
            to_return.append(temp)
   return to_return

def main():
   N = int(input("Enter N: "))
   print(solve(N))

def get_csp(N):
   count = 0
   csp_table = [set() for x in range(6*N - 2)]
   for col in range(N):
      csp_table[count] = set([col + x*N for x in range(N)])
      count += 1
   for row in range(N):
      csp_table[count] = set([row*N + x for x in range(N)])
      count += 1
   for x in range(N):
      row = 0
      col = x
      while row < N and col < N:
         csp_table[count].add(row*N + col)
         row += 1
         col += 1
      count += 1
   for x in range(1,N):
      row = x
      col = 0
      while row < N and col < N:
         csp_table[count].add(row*N + col)
         row += 1
         col += 1
      count += 1

   for x in range(N):
      row = 0
      col = x
      while row < N and col >= 0:
         csp_table[count].add(row*N + col)
         row += 1
         col -= 1
      count += 1
   for x in range(1,N):
      row = x
      col = N-1
      while row < N and col >= 0:
         csp_table[count].add(row*N + col)
         row += 1
         col -= 1
      count += 1

   return csp_table
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
      while index_row >= 0 and index_col < N:
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