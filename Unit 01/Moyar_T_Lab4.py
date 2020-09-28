#Trent Moyar
#Period 3

import pickle

''' helper methods goes here '''

def generate_path(current, explored):
   list = [current]
   count = 0
   while explored[current] != "":       #assume the parent of root is ""
      list.append(explored[current])
      current = explored[current]
      count += 1
   return (list[::-1], count+1)

def recur(start, end, word_dict, explored, limit):
   ''' your code goes here '''
   if start == end:
      return generate_path(start, explored)
   elif limit == 0:
      return None
   else:
      for temp in word_dict[start]:
         if not check(explored, start, temp):
            explored[temp] = start
            result = recur(temp, end, word_dict, explored, limit-1)
            if result != None:
               return result
      return None

def check(explored, current, new):
   temp = current
   while temp != "":
      if temp == new:
         return True
      temp = explored[temp]
   return False

def solve(start, end, word_dict, limit):
   explored = {start:""}
   return recur(start, end, word_dict, explored, limit-1)

def main():
   limit = int(input("Type the limit (1 - 20): "))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   word_dict = {}

   # You need to change the pickle file name
   with open("Moyar_T_Lab3.pkl", "rb") as infile:
      word_dict = pickle.load(infile)
   path_and_steps = (solve(initial, goal, word_dict, limit))
   solved = True
   if path_and_steps != None:
      print ("Path:", path_and_steps[0])
      print ("steps within {} limit:".format(limit), path_and_steps[1])
   else:
      solved = False
      print ("Solution not found in {} steps".format(limit))
   
   # Now, start iterative deepening
   for x in range(1 if solved else limit + 1,100):
      path = solve(initial, goal, word_dict, x)
      if path != None:
         print("Shortest Path:", path[0])
         print("Steps:", path[1])
         break
   # Print out the shortest path and length of the path (number of steps)
   

if __name__ == '__main__':
   main()

'''Type the limit (1 - 20): 10
Type the starting word: foiled
Type the goal word: cooper
Path: ['foiled', 'toiled', 'tailed', 'wailed', 'sailed', 'soiled',
'coiled', 'cooled', 'cooler', 'cooper']
steps within 10 limit: 10
Shortest Path: ['foiled', 'fooled', 'cooled', 'cooler', 'cooper']
Steps: 5'''