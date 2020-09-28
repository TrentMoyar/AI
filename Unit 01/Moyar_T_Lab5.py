# Name: Trent Moyar       
# Date: 9/19/2019


import math, random, time, heapq, string

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
      
   
   
def check_pq():
   ''' check_pq is checking if your PriorityQueue
   is completed or not'''
   pq = PriorityQueue()
   temp_list = []

   for i in range(10):
      a = random.randint(0,10000)
      pq.push(a)
      temp_list.append(a)

   temp_list.sort()   
   
   for i in temp_list:
      j = pq.pop()
      if not i == j:
         return False
   return True

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   for x in range(len(current)):
      for y in string.ascii_lowercase:
         s = replace(current,x,y)
         if (current[x] != y) & (s in words_set):
            adj_set.add(s)
   return adj_set
   
def replace(state, index, ch):
   '''your code goes here'''
   l = list(state)
   l[index] = ch
   return "".join(l)
def check_adj(words_set):
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def dist_heuristic(current, goal):
   ''' current and goal are words to compare. Calculate the heuristic function
   and then return a numeric value'''
   # TODO 3: heuristic
   # Your code goes here
   toreturn = 0
   for x in range(len(current)):
      toreturn += 0 if current[x] == goal[x] else 1
   return toreturn

def a_star(word_list, start, goal, heuristic=dist_heuristic):
   '''A* algorithm use the sum of cumulative path cost and the heuristic value for each loop
   Update the cost and path if you find the lower-cost path in your process.
   You may start from your BFS algorithm and expand to keep up the total cost while moving node to node.
   '''
   frontier = PriorityQueue()
   if start == goal: return []
   # TODO 4: A* Search
   # Your code goes here
   h = heuristic(start, goal)
   explored = {start: h}
   frontier.push((h, start, [start]))
   prev = ""
   while not frontier.isEmpty():
      t = frontier.pop()
      if t[1] == goal:
         return t[2]
      for x in generate_adjacents(t[1], word_list):
         if len(t[2]) > 1:
            if x == t[2][-2]:
               continue
         tup = (heuristic(x, goal) + len(t[2]), x, t[2] + [x])
         if x not in explored:
            frontier.push(tup)
            explored[x] = tup[0]
         elif tup[0] < explored[x]:
            frontier.push(tup)
            explored[x] = tup[0]
   return None

def main():
   print ("PriorityQueue() works:", check_pq())
   words_set = set()
   file = open("words_6_longer.txt", "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   print ("Check generate_adjacents():", check_adj(words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path_and_steps = (a_star(words_set, initial, goal))
   if path_and_steps != None:
      print (path_and_steps)
      print ("steps: ", len(path_and_steps))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''Sample output 1
PriorityQueue() works: True
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
steps:  7
Duration: 0.000997304916381836

Sample output 2
PriorityQueue() works: True
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
steps:  13
Duration: 0.0408782958984375

Sample output 3
PriorityQueue() works: True
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
steps:  19
Duration:  0.0867915153503418
'''


