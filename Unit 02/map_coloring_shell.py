# Name:
# Period:


def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 

   return True

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   pass

   
def isValid(value, var, assignment, variables, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   return True

def backtracking_search(variables, adjs): 
   return recursive_backtracking({}, variables, adjs)

def recursive_backtracking(assignment, variables, adjs):
   # Refer the pseudo code given in class.
   return None

def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   
   
   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = ['R', 'G', 'B']



   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.



   # solve the map coloring problem by using backtracking_search
   solution = backtracking_search(variables, adjacents)
   print (solution)

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'R', 'NT': 'G', 'SA': 'B', 'Q': 'R', 'NSW': 'G', 'V': 'R', 'T': 'R'}
By using graphics functions, visualize the map.
'''