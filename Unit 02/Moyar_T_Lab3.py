# Name: Trent Moyar
# Period: 3
import sys

def check_complete(assignment, regions, indices):
   # check if assignment is complete or not. Goal_Test 
   #for x in assignment
   if assignment == None:
      return False
   return "." not in assignment

def select_unassigned_var(assignment, regions, indices):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   #l = sorted(variables.keys(), key=lambda values: len(variables[values]), reverse=True)[0]
   #var = l[0]
   #forward checking
   for x in range(len(assignment)):
      if assignment[x] == ".":
         return x
   return None

def isValid(value, var, assignment, regions, indices):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   for x in regions[var]:
      temp = set()
      for y in indices[x]:
         temp.add(assignment[y])
      if value in temp:
         return False
   return True
 
def backtracking_search(sudoku, regions, indices): 
   return recursive_backtracking(sudoku, regions, indices)

def recursive_backtracking(assignment, regions, indices):
   # Refer the pseudo code given in class.
   if check_complete(assignment, regions, indices):
      return assignment
   var = select_unassigned_var(assignment, regions, indices)
   for value in range(1,10):
      if isValid(str(value),var,assignment,regions, indices):
         l = list(assignment)
         l[var] = str(value)
         assignment = "".join(l)
         result = recursive_backtracking(assignment, regions, indices)
         if check_complete(result, regions, indices):
            return result
         l = list(assignment)
         l[var] = "."
         assignment = "".join(l)
   return None

def main():
   counter = 0
   indices = {}
   regions = {}
   for w in range(0,3):
      for x in range(0,3):
         indices[counter] = []
         for y in range(0,3):
            for z in range(0,3):
               indices[counter].append(z + 9*y + 27*w + x*3)
         counter += 1
   for row in range(0,9):
      indices[counter] = [row*9 + x for x in range(0,9)]
      counter += 1
   for col in range(0,9):
      indices[counter] = [x*9 + col for x in range(0,9)]
      counter += 1
   for region in indices:
      for index in indices[region]:
         if index not in regions:
            regions[index] = [region]
         else:
            regions[index].append(region)

   solution = backtracking_search(sys.argv[1], regions, indices)
   for x in range(0,9):
      print(solution[x*9:x*9+9])

if __name__ == '__main__':
   main()