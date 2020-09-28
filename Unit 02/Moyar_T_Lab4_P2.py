#Trent Moyar
#Period 3
import string
import sys
import copy
import time

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
   min_pos = 0
   min_value = 10000
   for x in variables:
      if len(variables[x]) < min_value:
         min_pos = x
         min_value = len(variables[x])
   return min_pos
   '''
   max(q_table, key=q_table.get)
   findings = [x for x in range(len(pzl)) if pzl[x] == max_val]
   no_go = set()
   for x in findings:
      no_go |= NEIGHBORS[x]
   return (set(range(len(pzl))) - no_go).pop()
   '''
def resolve_definites(pzl, NEIGHBORS, variables, q_table, N, all_chars):
   eights = set()
   for x in q_table:
      if q_table[x] == all_chars[-2]:
         eights.add(x)
   toreturn = set()
   toremove = set()
   for x in variables:
      for h in eights:
         if h in variables[x]:
            pzl[x] = h
            toremove.add(x)
      if len(variables[x]) == 1:
         for z in variables[x]:
            pzl[x] = z
            toremove.add(x)
            for y in NEIGHBORS[x]:
               if pzl[y] == '.':
                  variables[y].discard(z)
   for x in toremove:
      del variables[x]
def recursive_backtracking(added_index, added_value, pzl, NEIGHBORS, variables, q_table, N, all_chars,d):
   resolve_definites(pzl, NEIGHBORS, variables, q_table, N, all_chars)
   if added_index != None and added_index in variables:
      pzl[added_index] = added_value
      del variables[added_index]
      for x in NEIGHBORS[added_index]:
         if x in variables:
            variables[x].discard(added_value)
            if len(variables[x]) == 0:
               return None
      q_table[added_value] += 1
   if is_complete(pzl):
      return pzl
   v = select_var(pzl, NEIGHBORS, variables, q_table, all_chars)
   temp = sorted(variables[v],key=q_table.get,reverse=True)
   for c in temp:
      result = recursive_backtracking(v,c,pzl[:], NEIGHBORS, {x:variables[x].copy() for x in variables}, q_table.copy(), N, all_chars,d + 1)
      if result != None:
         return result
   return None
def is_complete(pzl):
   if pzl == None:
      return False
   return '.' not in pzl
def solve(pzl,N):
   all_chars = []
   chars_to_15 = [str(x) for x in range(1,10)] + list(string.ascii_uppercase)
   chars_16_to = [str(x) for x in range(0,10)] + list(string.ascii_uppercase)
   if N < 16:
      all_chars = [str(chars_to_15[x]) for x in range(0,N)]
   else:
      all_chars = [str(chars_16_to[x]) for x in range(0,N)]
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
   variables = {x:set(all_chars) - set([pzl[y] for y in NEIGHBORS[x] if pzl[y] != '.']) for x in linear_list if pzl[x] == '.'}
   q_table = {x:0 for x in all_chars} # N keys
   for x in pzl:
      if x != '.':
         q_table[x] += 1
   temp = recursive_backtracking(None, None, list(pzl), NEIGHBORS, variables, q_table, N, all_chars,0)
   return temp
   
def main():
   cur_time = time.time()
   puzzles = open(input("enter puzzle list: "))
   pzls = []
   for x in puzzles.readlines():
      pzls.append(x.rstrip('\n'))
   puzzles.close()
   for x in range(len(pzls)):
      N = int(len(pzls[x])**0.5)
      print(pzls[x])
      temp = solve(pzls[x],N)
      print(str(x) + ":" + str(check_sum(temp,N)) + "  " + str("".join(temp)))
   print ("Duration: ", (time.time() - cur_time))



if __name__ == '__main__':
   main()