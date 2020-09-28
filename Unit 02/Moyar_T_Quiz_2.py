#Trent Moyar
#10/31/2019
#Unit 2 Quiz 2

def check_complete(assignment, adjacents):
   # check if assignment is complete or not. Goal_Test 
   #for x in assignment
   if assignment == None:
      return False
   edgeset = set()
   for x in assignment:
      for y in adjacents[x]:
         edgeset.add(y)
   for x in range(0,20):
      c = 0
      for y in adjacents[x]:
         if (x not in assignment) and (y not in assignment):
            c += 1
      if c == 3:
         return False
   return True

def select_unassigned_var(assignment, variables):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   #l = sorted(variables.keys(), key=lambda values: len(variables[values]), reverse=True)[0]
   #var = l[0]
   #forward checking
   for x in range(0,20):
      if x not in assignment:
         return x
   return None

def isValid(nuset, adjacents):
   edgeset = set()
   for x in nuset:
      for y in adjacents[x]:
         edgeset.add(y)
   for x in edgeset:
      if x in nuset:
         return False
   return True


def backtracking_search(assignment,solutions, adjacents): 
   return recursive_backtracking(assignment, solutions, adjacents,0)

def recursive_backtracking(assignment, solutions, adjacents,max):
   # Refer the pseudo code given in class.
   # Code doesn't stop, prints solutions, I had to find greatest
   thismax = max
   if check_complete(assignment, adjacents):
      print(assignment)
      solutions.append(assignment)
      return None
   for x in range(0,20):
      if x not in assignment:
         assignment.append(x)
         if isValid(assignment, adjacents):
            recursive_backtracking(assignment.copy(), solutions, adjacents, thismax)
         del assignment[-1]
   return None

def main():
   adjacents = {1:set([8]),2:set([6]),13:set([9]),14:set([7]),5:set([15]),16:set([12]),10:set([0]),19:set([3,0]),4:set([17]),18:set([11])}
   for x in range(0,19):
      if x in adjacents:
         adjacents[x].add(x+1)
      else:
         adjacents[x] = set([x+1])
   for x in adjacents:
      for y in adjacents[x]:
         adjacents[y].add(x)
   
   solutions = []
   backtracking_search([],solutions, adjacents)
   print(sorted(solutions,key=len)[-1])

   

if __name__ == '__main__':
   main()