#Trent Moyar
#Period 3
import math
def is_not_valid(board, csp_table, N):
   for x in range(N*2):
      valid = False
      for y in csp_table[x]:
         if board[y] != -1:
            valid = True
      if valid == False:
         return True
   sum = 0
   for x in range(N*2, 4*N-1):
      valid = False
      for y in csp_table[x]:
         if board[y] != -1:
            valid = True
      if valid == False:
         sum += 1
   if sum > N - 1:
      return True
   sum = 0
   for x in range(4*N-1, 6*N-2):
      valid = False
      for y in csp_table[x]:
         if board[y] != -1:
            valid = True
      if valid == False:
         sum += 1
   if sum > N - 1:
      return True
   return False

def recur_solve(added, board, NEIGHBORS, csp_table, N, d):
   if added != None:
      board[added] = 1
      for x in NEIGHBORS[added]:
         if board[x] == 0:
            board[x] = -1
   if is_not_valid(board, csp_table,  N):
      return None
   if d == N:
      return board
   col = select_col(board, csp_table, N)
   vars = select_vars(board, NEIGHBORS, csp_table[col], N)
   for x in vars:
      result = recur_solve(x, board[:], NEIGHBORS, csp_table, N, d + 1)
      if result != None:
         return result
   return None
def select_col(board, csp_table, N):
   sum = [0 for x in range(N)]
   for x in range(N):
      for y in csp_table[x]:
         if board[y] == 1:
            sum[x] = N
            break
         if board[y] == 0:
            sum[x] += 1
   pos = 0
   mini = N*N*2
   for x in range(N):
      if sum[x] < mini:
         mini = sum[x]
         pos = x
   return pos
def select_vars(board, NEIGHBORS, indices, N):
   poss = [x for x in indices if board[x] == 0]
   return sorted(poss, key = lambda yeet: find_affected(yeet,board,NEIGHBORS))

def find_affected(index, board, NEIGHBORS):
   summ = 0
   for x in NEIGHBORS[index]:
      if board[x] == 0:
         summ += board[x]
   return summ
def main():
   N = int(input("Input N: "))
   csp_table = get_csp(N)
   neighbors = create_neighbors(N)
   board = [0 for y in range(N*N)]
   display(recur_solve(None, board[:], neighbors, csp_table, N, 0), N)
   print(N)

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
   string = "".join(str(x) for x in board)
   string = string.replace("-1", ".")
   for x in range(N):
      print(string[x*N:x*N+N])
if __name__ == '__main__':
   main()