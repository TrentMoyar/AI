# Name: Trent Moyar         
# Date: 9/26/2019
import heapq
import random, time, math

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
      del self.queue[index]
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

def inversion_count(new_state, width, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
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
   if N%2 == 1:
      return invert%2 == 0         
   return (new_state.find("_")%(width*2) >= width) == (invert%2 == 1)

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)


def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
def swap(n, i, j):
   # Your code goes here
   l = list(n)
   l[i], l[j] = l[j], l[i]
   return "".join(l)
      
def generateChild(node, size):
   # Your code goes here
   space = node.find("_")
   toreturn = []
   if((space + size) < size ** 2):
      toreturn.append(swap(node,space, space + size)) #swap with next row
   if((space - size) >= 0):
      toreturn.append(swap(node,space, space - size)) #swap with previous row
   if(space%size < (size - 1)):
      toreturn.append(swap(node,space, space+1))  #swap with next char
   if(space%size > 0):
      toreturn.append(swap(node,space, space-1)) #swap with prev char
   return toreturn

def display_path(path_list, size):
   for n in range(size):
      for i in range(len(path_list)):
         print (path_list[i][n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''

def dist_heuristic(start, goal, size):
   # Your code goes here
   
   dist = 0
   pos = 0
   dict = {goal[x] : x for x in range(size**2)}

   for x in range(size**2):
      if goal[x] != start[x]:
         pos = dict[start[x]]
         dist += abs(int(x/size) - int(pos/size)) + abs(x%size - pos%size)
   return dist

def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b) 
def tolist(dict, start, goal):
   cur = goal
   toreturn = [cur]
   while cur != start:
      cur = dict[cur][1]
      toreturn.append(cur)
   toreturn.reverse()
   return toreturn

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4): 
   
   frontier = PriorityQueue()
   heur = {}
   adj = {}
   if start == goal: return []
   # Your code goes here
   if not inversion_count(start,size):
      return None
   heur[start] = heuristic(start,goal,size)
   s = (heur[start],start,0)
   frontier.push(s)
   explored = {start : (s[0], None)}
   tup = None
   # Your code goes here
   while not frontier.isEmpty():
      s = frontier.pop()
      if s[1] == goal:
         return tolist(explored, start, goal)
      #print(s[1])
      for x in generateChild(s[1],size):
         if x != explored[s[1]][1]:
            if x not in heur:
               heur[x] = heuristic(x,goal,size)
            tup = (heur[x] + s[2], x, s[2] + 1)
            if (x not in explored) or (explored[x][0] > tup[0]):
               explored[x] = (tup[0],s[1])
               frontier.push(tup)  

def main():
    # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   initial_state = input("Initial State: ")
   cur_time = time.time()
   path = (a_star(initial_state))
   if path != None: display_path(path, 4)
   else: print ("No Path Found.")
   print ("Duration: ", (time.time() - cur_time))

if __name__ == '__main__':
   main()


''' Sample output 1

Inversion works?: True
Initial State: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0


Sample output 2

Inversion works?: True
Initial State: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005014657974243164


Sample output 3

Inversion works?: True
Type initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.27825474739074707


Sample output 4

Inversion works?: True
Type initial state: 8293AC4671FEDB5_
8293    8293    8293    8293    8293    8293    8293    8293    82_3    8_23    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
AC46    AC46    AC46    AC46    AC46    _C46    C_46    C4_6    C496    C496    C_96    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
71FE    71F_    71_F    7_1F    _71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5_    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 39
Duration:  0.7709157466888428

'''

