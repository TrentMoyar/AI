# Name: Trent Moyar
# Period: 3
from tkinter import *
from graphics import *

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
   #for x in assignment
   return len(assignment) == len(vars)

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   #l = sorted(variables.keys(), key=lambda values: len(variables[values]), reverse=True)[0]
   #var = l[0]
   #forward checking
   '''
   for x in vars:
      if x not in assignment:
         return x
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

   
   

   
def isValid(value, var, assignment, variables, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   for x in adjs[var]:
      if x in assignment:
         if assignment[x] == value:
            return False
   return True

def backtracking_search(variables, adjs, map): 
   return recursive_backtracking({}, variables, adjs, map)

def recursive_backtracking(assignment, variables, adjs, map):
   # Refer the pseudo code given in class.
   if check_complete(assignment, variables, adjs):
      return assignment
   var = select_unassigned_var(assignment, variables, adjs)
   for value in variables[var]:
      time.sleep(0.2)
      if isValid(value,var,assignment,variables,adjs):
         assignment[var] = value
         map[var].setFill(valtocol(value))
         result = recursive_backtracking(assignment, variables, adjs, map)
         if check_complete(result, variables, adjs):
            return result
         del assignment[var]
         map[var].setFill("white")
   return None
def valtocol(val):
   switcher = {
      'R': 'red',
      'G': 'green',
      'B': 'blue'
   }
   return switcher[val]
def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   nodes = open("mcNodes.txt")
   for x in nodes.readlines():
      regions.append(x.rstrip('\n'))
      adjacents[x.rstrip('\n')] = []
   nodes.close()
   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = ['R', 'G', 'B']
   


   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   adj = open("mcEdges.txt")
   for x in adj.readlines():
      temp = x.rstrip('\n').split()
      adjacents[temp[0]].append(temp[1])
      adjacents[temp[1]].append(temp[0])
   adj.close()

   frame = GraphWin('Map', 833, 755)
   #frame.setCoords(0, 0, 832, 754)
   map = open("map.txt")
   shapes = {}
   for x in map.readlines():
      temp = x.rstrip('\n').split()
      shapes[temp[0]] = polygon(temp[1:])
   for x in shapes:
      shapes[x].setFill("white")
      shapes[x].setOutline("black")
      shapes[x].draw(frame)
      
   # solve the map coloring problem by using backtracking_search
   solution = backtracking_search(variables, adjacents, shapes)
   print (solution)
   mainloop()

def polygon(s):
   toreturn = []
   for x in s:
      y = x.split(",")
      print(int(y[1][0:-1]))
      toreturn.append(Point(int(y[0][1:]),int(y[1][0:-1])))
   return Polygon(*toreturn)

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'R', 'NT': 'G', 'SA': 'B', 'Q': 'R', 'NSW': 'G', 'V': 'R', 'T': 'R'}
By using graphics functions, visualize the map.
'''