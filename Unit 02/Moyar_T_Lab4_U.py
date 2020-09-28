#Trent Moyar
#Period 3
import string
import sys

def check_sum(solution,N):
   ascii_sum = sum([ord(solution[p]) for p in range(N*N)])
   ascii_sum -= 48*N*N
   return ascii_sum
def nearest_factor(factor):
   square = int(factor**0.5)
   for x in range(square,0,-1):
      if factor%x == 0:
         return x
def select_var(pzl, NEIGHBORS, variables, q_table, all_chars):
   values = []
   maxi = (0,0)
   for x in range(len(pzl)):
      if pzl[x] == '.':
         temp = len(variables[x])# * max([q_table[x] for x in taken])
         if temp > maxi[1]:
            maxi = (x,temp)
   #print(sorted(maxi[2],key=lambda x:q_table[x],reverse=True))
   return maxi[0]
def recursive_backtracking(pzl, NEIGHBORS, variables, q_table, N, all_chars):
   if is_complete(pzl):
      return pzl
   v = select_var(pzl, NEIGHBORS, variables, q_table, all_chars)
   for c in variables[v]:
      if is_valid(v,c,pzl,NEIGHBORS,q_table,N):
         q_table[c] += 1
         pzl[v] = c
         update_variables(variables, NEIGHBORS, pzl, all_chars)
         result = recursive_backtracking(pzl[:], NEIGHBORS, variables, q_table.copy(), N, all_chars)
         if result:
            return result
         pzl[v] = '.'
         update_variables(variables, NEIGHBORS, pzl, all_chars)
         q_table[c] -= 1
   return None
def update_variables(variables, NEIGHBORS, pzl, all_chars):
   variables = {x:all_chars - set([pzl[y] for y in NEIGHBORS[x] if pzl[y] != '.']) for x in range(len(pzl)) if pzl[x] == '.'}
def is_valid(var, value, pzl, NEIGHBORS, q_table, N):
   if q_table[value] > N**2:
      return False
   for index in NEIGHBORS[var]:
      if pzl[index] == value:
         return False
   return True
def is_complete(pzl):
   if pzl == None:
      return False
   return '.' not in pzl
def solve(pzl,N):
   chars = [str(x) for x in range(1,10)] + list(string.ascii_uppercase)
   all_chars = set([str(chars[x]) for x in range(0,N)])
   linear_list = [a for a in range(N*N)]
   each_row = [[x+i*N for x in range(N)] for i in range(N)]
   each_col = [linear_list[col::N] for col in range(N)]
   counter = 0
   each_subBlock = []
   height = nearest_factor(N)
   width = int(N/height)
   for w in range(0,width):
      for x in range(0,height):
         each_subBlock.append([])
         for y in range(0,height):
            for z in range(0,width):
               each_subBlock[counter].append(z + N*y + N*height*w + x*width)
         counter += 1
   csp_table = each_row + each_col + each_subBlock
   NEIGHBORS = {x:set() for x in linear_list}
   for x in linear_list:
      for y in csp_table:
         if x in y:
            temp = y[:]
            temp.remove(x)
            NEIGHBORS[x].update(temp)
   variables = {x:all_chars - set([pzl[y] for y in NEIGHBORS[x] if pzl[y] != '.']) for x in linear_list if pzl[x] == '.'}
   q_table = {x:0 for x in all_chars} # N keys
   for x in pzl:
      if x != '.':
         q_table[x] += 1
   temp = recursive_backtracking(list(pzl), NEIGHBORS, variables, q_table, N, all_chars)
   print(variables)
   #print(str(x) + ":" + "".join(temp))
   return temp
   
def main():
   puzzles = open(input("enter puzzle list: "))
   pzls = []
   for x in puzzles.readlines():
      pzls.append(x.rstrip('\n'))
   puzzles.close()
   for x in range(len(pzls)):
      N = int(len(pzls[x])**0.5)
      print(str(x) + ":" + str(solve(pzls[x],N)))



if __name__ == '__main__':
   main()