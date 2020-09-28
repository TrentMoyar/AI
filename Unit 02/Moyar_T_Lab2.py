# Name: Trent Moyar
# Period: 3
import sys

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
   #for x in assignment
   if assignment == None:
      return False
   return "." not in assignment

def select_unassigned_var(assignment, hexes, indices):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   #l = sorted(variables.keys(), key=lambda values: len(variables[values]), reverse=True)[0]
   #var = l[0]
   #forward checking
   for x in range(len(assignment)):
      if assignment[x] == ".":
         return x
   return None
   '''
   #MRV
   minchoice = {}
   for x in vars:
      if x not in assignment:
         minchoice[x] = set()
         for y in adjs[x]:
            if y in assignment:
               minchoice[x].add(assignment[y])
   print(minchoice)
   l = [(x,y) for x,y in minchoice.items()]
   l.sort(key=lambda s:len(s[1]))
   return(l[-1][0])
   '''

def isValid(value, var, assignment, hexes, indices):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   for x in hexes[var]:
      temp = set()
      for y in indices[x]:
         temp.add(assignment[y])
      if value in temp:
         return False
   return True

def backtracking_search(hexagon, hexes, indices): 
   return recursive_backtracking(hexagon, hexes, indices)

def recursive_backtracking(assignment, hexes, indices):
   # Refer the pseudo code given in class.
   if check_complete(assignment, hexes, indices):
      return assignment
   var = select_unassigned_var(assignment, hexes, indices)
   for value in range(1,7):
      if isValid(str(value),var,assignment,hexes, indices):
         l = list(assignment)
         l[var] = str(value)
         assignment = "".join(l)
         result = recursive_backtracking(assignment, hexes, indices)
         if check_complete(result, hexes, indices):
            return result
         l = list(assignment)
         l[var] = "."
         assignment = "".join(l)
   return None

def main():
   indices = {
      0:[0,1,2,6,7,8],
      1:[2,3,4,8,9,10],
      2:[9,10,11,16,17,18],
      3:[15,16,17,21,22,23],
      4:[13,14,15,19,20,21],
      5:[5,6,7,12,13,14],
      6:[7,8,9,14,15,16]
   }
   hexes = {x : set() for x in range(24)}
   for x in indices:
      for y in indices[x]:
         hexes[y].add(x)
   solution = backtracking_search(sys.argv[1], hexes, indices)

   print("",solution[0:5],"")
   print(solution[5:12])
   print(solution[12:19])
   print("",solution[19:24],"")

if __name__ == '__main__':
   main()