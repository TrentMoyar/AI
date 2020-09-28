# Name: Trent Moyar
# Period: 3
import sys
import string

class Board:
   def __init__(self, initial):
      counter = 0
      #initialize dictionary to convert regions into the indices that they contain
      self.region_to_indices = {}
      #initialize dictionary to convert indices into the regions that contain them
      self.index_to_regions = {}
      self.index_to_affected = {x:set() for x in range(0,len(sys.argv[1]))}
      self.N  = int(len(sys.argv[1])**0.5)
      self.region_quantities = {}
      self.possible_values = {}
      chars = list(range(1,10)) + list(string.ascii_uppercase)
      self.all_chars = set([str(chars[x]) for x in range(0,self.N)])
      height = nearestFactor(self.N)
      width = int(self.N/height)
      for w in range(0,width):
         for x in range(0,height):
            self.region_to_indices[counter] = []
            self.region_quantities[counter] = {x:0 for x in self.all_chars}
            for y in range(0,height):
               for z in range(0,width):
                  self.region_to_indices[counter].append(z + self.N*y + self.N*height*w + x*width)
            counter += 1
      for row in range(0,self.N):
         self.region_to_indices[counter] = [row*self.N + x for x in range(0,self.N)]
         self.region_quantities[counter] = {x:0 for x in self.all_chars}
         counter += 1
      for col in range(0,self.N):
         self.region_to_indices[counter] = [x*self.N + col for x in range(0,self.N)]
         self.region_quantities[counter] = {x:0 for x in self.all_chars}
         counter += 1
      for region in self.region_to_indices:
         for index in self.region_to_indices[region]:
            if index not in self.index_to_regions:
               self.index_to_regions[index] = [region]
            else:
               self.index_to_regions[index].append(region)
      for x in self.index_to_affected:
         for y in self.index_to_regions[x]:
            for z in self.region_to_indices[y]:
               self.index_to_affected[x].add(z)
      self.values = list(initial)
      self.full_update()
   def full_update(self):
      for x in range(0,len(self.values)):
         new_set = set()
         for z in self.index_to_affected[x]:
            new_set.add(self.values[z])
         self.possible_values[x] = self.all_chars - new_set
         for y in self.possible_values[x]:
            for z in self.index_to_regions[x]:
               self.region_quantities[z][y] += 1
   def add(self, value, index):
      value = str(value)
      self.update_value(index, self.values[index], value)
   def remove(self, index):
      index = int(index)
      self.update_value(index, self.values[index], ".")
   def update_value(self,index,prev,new):
      index = int(index)
      prev = str(prev)
      new = str(new)
      self.values[index] = new
      '''
      if prev is not ".":
         for x in self.index_to_affected[index]:
            b = True
            for y in self.index_to_affected[x]:
               if self.values[y] == prev:
                  b = False
                  break
            if b:
               if prev not in self.possible_values[x]:
                  for y in self.index_to_regions[x]:
                     self.region_quantities[y][prev] += 1
               self.possible_values[x].add(prev)
               
      if new is not ".":
         for x in self.index_to_affected[index]:
            if new in self.possible_values[x]:
               for y in self.index_to_regions[x]:
                  self.region_quantities[y][new] -= 1
            self.possible_values[x].discard(new)'''
      self.full_update()
   def definites(self):
      toreturn = {}
      for x in self.region_quantities:
         for y in self.region_quantities[x]:
            if self.region_quantities[x][y] is 1:
               for z in self.region_to_indices[x]:
                  if y in self.possible_values[z] and self.values[z] is ".":
                     toreturn[z] = y
      for x in self.possible_values:
         if len(self.possible_values[x]) is 1 and self.values[x] is ".":
            toreturn[x] = list(self.possible_values[x])[0]
      return toreturn
   def ordered_indef(self):
      toreturn = []
      for x in range(0,len(self.values)):
         if self.values[x] is ".":
            toreturn.append(x)
      return sorted(toreturn,key=lambda yeet: len(self.possible_values[yeet]))
      #return {x:self.values[x] for x in range(0,self.N)}
      '''
      toreturn = {}
      for x in self.region_quantities:
         for y in self.region_quantities[x]:
            if self.region_quantities[x][y] is (self.N-1):
               for z in self.region_to_indices[x]:
                  if y in self.possible_values[z] and self.values[z] is ".":
                     toreturn[z] = y
      for x in self.possible_values:
         if len(self.possible_values[x]) is 1 and self.values[x] is ".":
            toreturn[x] = list(self.possible_values[x])[0]
      return toreturn
      '''
   def is_valid(self):
      for x in range(0,len(self.values)):
         for y in self.index_to_affected[x]:
            if (self.values[x] is not ".") and (self.values[x] is self.values[y]) and (x is not y):
               return False
      return True
   def is_complete(self):
      return "." not in self.values
   def not_possible(self):
      for x in range(0,len(self.values)):
         if self.values[x] is "." and len(self.possible_values[x]) > 0:
            return False
      return True
   def __str__(self):
      toreturn = ""
      counter = 0
      for x in range(0,self.N):
         for y in range(0,self.N):
            toreturn += self.values[counter]
            counter += 1
         toreturn += "\n"
      return toreturn
   def copy(self):
      toreturn = Board("".join(self.values))
      toreturn.values = self.values.copy()
      toreturn.N = self.N
      toreturn.all_chars = self.all_chars.copy()
      toreturn.index_to_affected = self.index_to_affected.copy()
      toreturn.region_quantities = self.region_quantities.copy()
      toreturn.region_to_indices = self.region_to_indices.copy()
      toreturn.index_to_regions = self.index_to_regions.copy()
      toreturn.possible_values = self.possible_values.copy()
      return toreturn
def select_unassigned_var(assignment, index_to_regions, region_to_indices, N):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   #l = sorted(variables.keys(), key=lambda values: len(variables[values]), reverse=True)[0]
   #var = l[0]
   #forward checking
   for x in range(len(assignment)):
      if assignment[x] == ".":
         return x
   return None
 
def backtracking_search(board): 
   return recursive_backtracking(board)

def recursive_backtracking(board):
   # Refer the pseudo code given in class.
   
   defini = board.definites()
   while len(defini) > 0:
      for x in defini:
         board.add(defini[x],x)
      defini = board.definites()
    
   if board.is_complete():
      return board
   if board.not_possible():
      return None
   indef = board.ordered_indef()
   for index in indef:
      temp = board.possible_values[index].copy()
      for y in temp:
         board.add(y,index)
         if board.is_valid():
            result = recursive_backtracking(board.copy())
            if result and result.is_complete():
               return result
         board.remove(index)
   return None
def nearestFactor(factor):
   square = int(factor**0.5)
   for x in range(square,0,-1):
      if factor%x == 0:
         return x
def main():
   b = Board(sys.argv[1])
   print(b)
   print(b.possible_values)
   print(backtracking_search(b))
 
   '''
   solution = backtracking_search(sys.argv[1], index_to_regions, region_to_indices, N)
   for x in range(0,N):
      print(solution[x*N:x*N+N])'''
if __name__ == '__main__':
   main()