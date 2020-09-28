#Trent Moyar
#10/31/2019
#Unit 2 Quiz 1

def check_complete(assignment):
   # check if assignment is complete or not. Goal_Test 
   #for x in assignment
   if assignment == None:
      return False
   return len(assignment) == 5

def select_unassigned_var(assignment, variables):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   #l = sorted(variables.keys(), key=lambda values: len(variables[values]), reverse=True)[0]
   #var = l[0]
   #forward checking
   for x in variables:
      if x not in assignment:
         return x
   return None

def isValid(assignment):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   l = sorted(assignment.values())
   for x in range(2,len(l))[::-1]:
      l[x] = l[x] - l[x-1]
   dists = []
   for i, v in enumerate(l):
      if i > 1:
         temp = []
         for x in range(1,i):
            temp.append(v + dists[-x])
         dists = dists + temp
         dists.append(v)
      else:
         dists.append(v)
   valid = set()
   for x in dists:
      if x in valid:
         return False
      valid.add(x)
   return True

def backtracking_search(assignment, variables): 
   return recursive_backtracking(assignment, variables)

def recursive_backtracking(assignment, variables):
   # Refer the pseudo code given in class.
   #print(assignment)
   if check_complete(assignment):
      return assignment
   var = select_unassigned_var(assignment, variables)
   for value in range(1,12):
      assignment[var] = value
      if isValid(assignment):
         result = recursive_backtracking(assignment.copy(), variables)
         if check_complete(result):
            return result
      del assignment[var]
   return None
def main():
   assignment = {'T':0}
   variables = set(['A','B','C','D'])
   #just one
   print(backtracking_search(assignment, variables))

   

if __name__ == '__main__':
   main()