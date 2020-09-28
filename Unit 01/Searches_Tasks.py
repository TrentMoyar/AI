# Name: Trent Moyar
# Period: 3
import random
import itertools
from collections import deque


def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return y
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j):
   '''your code goes here'''
   l = list(state)
   l[i], l[j] = l[j], l[i]
   return "".join(l)
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
   '''your code goes here'''
   space = state.find("_")
   toreturn = []
   if((space + 3) <= 8):
      toreturn.append(swap(state,space, space+3))
   if((space - 3) >= 0):
      toreturn.append(swap(state,space, space-3))
   if(space%3 < 2):
      toreturn.append(swap(state,space, space+1))
   if(space%3 > 0):
      toreturn.append(swap(state,space, space-1))
   return toreturn
   
def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   print ("\n\nThe shortest path length is :", len(l))
   return ""

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling generate_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state, goal):
   frontier = deque([initial_state])
   explored = {initial_state:"s"}
   '''Your code goes here'''
   while(len(frontier) != 0):
      temp = frontier.popleft()
      if(temp == goal):
         print("bfs length:",len(explored))
         return ""#display_path(temp, explored)
      for x in generate_children(temp):
         if (x not in explored):
            frontier.append(x)
            explored[x] = temp
   bfs_length = len(explored)
   print("bfs length:",len(explored))
   return ("No solution")
   
def findconnectable(initial_state):
   frontier = deque([initial_state])
   explored = {initial_state:"s"}
   '''Your code goes here'''
   while(len(frontier) != 0):
      temp = frontier.popleft()
      for x in generate_children(temp):
         if (x not in explored):
            frontier.append(x)
            explored[x] = temp
   bfs_length = len(explored)
   print("connected:",len(explored))

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling generate_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial):
   frontier = [initial]
   explored = {initial:"s"}
   '''Your code goes here'''
   while(len(frontier) != 0):
      temp = frontier.pop()
      if(temp == "_12345678"):
         print("dfs length:",len(explored))
         return ""#display_path(temp, explored)
      for x in generate_children(temp):
         if (x not in explored):
            frontier.append(x)
            explored[x] = temp
   dfs_length = len(explored)
   print("dfs length:",len(explored))
   return ("No solution")


def main():
   print(findconnectable("_12345678"))

if __name__ == '__main__':
   main()
