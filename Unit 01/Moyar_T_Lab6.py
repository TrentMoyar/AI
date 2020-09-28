# Name: Trent Moyar
# Date: 9/25/19
import heapq
import random, time, math, heapq

class PriorityQueue():
   def __init__(self):
      self.queue = []
      current = 0      # to make this object iterable
   
   # To make this object iterable: have __iter__ function and assign next function for __next__
   def next(self):
      if self.current >=len(self.queue):
         self.current
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 0

   ''' complete the following functions '''
   def remove(self, index):
      # remove self.queue[index]
      self.queue.pop(index)
      heapq.heapify(self.queue)
            
   def pop(self):
      # swap first and last. Remove last. Heap down from first.
      # return the removed value
      return heapq.heappop(self.queue)
      
            
   def push(self, value):
      # append at last. Heap up.
      heapq.heappush(self.queue, value)
      
   def peek(self):
      # return min value (index 0)
      return self.queue[0]

def inversion_count(new_state, size):
   ''' Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   # Your code goes here
   invert = 0
   new_s = new_state.replace("_", "")
   for x in range(len(new_s)):
      for y in range(x):
         if new_s[y] > new_s[x]:
            invert += 1
   if size%2 == 1:
      return invert%2 == 0         
   return (new_state.find("_")%(size*2) >= size) == (invert%2 == 1)
   
def check_inversion():
   t1 = inversion_count("_42135678", 3)
   f1 = inversion_count("21345678_", 3)
   return t1 and not f1

def getInitialState(sample):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   if(inversion_count(new_state, 3)): return new_state
   else: return None
   
def swap(n, i, j):
   # Your code goes here
   l = list(n)
   l[i], l[j] = l[j], l[i]
   return "".join(l)
      
def generateChild(n, size):
   # Your code goes here
   space = n.find("_")
   toreturn = []
   if((space + size) < size ** 2):
      toreturn.append(swap(n,space, space + size))
   if((space - size) >= 0):
      toreturn.append(swap(n,space, space - size))
   if(space%size < (size - 1)):
      toreturn.append(swap(n,space, space+1))
   if(space%size > 0):
      toreturn.append(swap(n,space, space-1))
   return toreturn

def display_path(path_list, size):
   for n in range(size):
      for i in range(len(path_list)):
         print (path_list[i][n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

def dist_heuristic(start, goal, size):
   # Your code goes here
   dist = 0
   pos = 0
   for x in range(len(goal)):
      pos = start.find(goal[x])
      dist += abs(x/size - pos/size) + abs(x%size - pos%size)
   return dist

def a_star(start, goal="_12345678", heuristic=dist_heuristic):
   frontier = PriorityQueue()
   if start == goal: return []
   size = 3
   if not inversion_count(start,size):
      return None
   frontier.push((heuristic(start,goal,size),start,[start]))
   explored = {start : heuristic(start,goal,size)}
   # Your code goes here
   while not frontier.isEmpty():
      s = frontier.pop()
      if s[1] == goal:
         return s[2]
      for x in generateChild(s[1],size):
         tup = (heuristic(x,goal,size) + len(s[2]), x, s[2] + [x])
         if x not in explored or explored[x] < tup[0]:
            explored[x] = tup[0]
            frontier.push(tup)   
   return None

def main():
    # A star
   print ("Inversion works?:", check_inversion())
#   initial_state = getInitialState("_12345678")
#   while initial_state == None:
#      initial_state = getInitialState("_12345678")
   initial_state = input("Type initial state: ")
   cur_time = time.time()
   path = (a_star(initial_state))
   if path != None: display_path(path, 3)
   else: print ("No Path Found.")
   print ("Duration: ", (time.time() - cur_time))

if __name__ == '__main__':
   main()

''' Sample output 1:

Inversion works?: True
Type initial state: 76423_581
764   764   764   764   764   _64   6_4   64_   641   641   641   641   641   _41   4_1   431   431   431   431   _31   3_1   31_   312   312   312   _12   
23_   231   231   2_1   _21   721   721   721   72_   7_2   732   732   _32   632   632   6_2   652   652   _52   452   452   452   45_   4_5   _45   345   
581   58_   5_8   538   538   538   538   538   538   538   5_8   _58   758   758   758   758   7_8   _78   678   678   678   678   678   678   678   678   

The shortest path length is : 26
Duration:  0.06485509872436523


Sample output 2:

Inversion works?: True
Type initial state: 84765231_
847   847   847   847   _47   4_7   47_   472   472   472   472   472   472   472   472   472   472   472   472   472   472   4_2   _42   142   142   142   142   1_2   _12   
652   652   6_2   _62   862   862   862   86_   861   861   8_1   _81   381   381   3_1   31_   315   315   315   _15   1_5   175   175   _75   375   375   3_5   345   345   
31_   3_1   351   351   351   351   351   351   35_   3_5   365   365   _65   6_5   685   685   68_   6_8   _68   368   368   368   368   368   _68   6_8   678   678   678   

The shortest path length is : 29
Duration:  0.28726887702941895

'''
