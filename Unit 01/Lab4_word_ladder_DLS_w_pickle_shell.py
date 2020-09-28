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
   return None
 
 
def solve(start, end, word_dict, limit):
   explored = {start:""}
   return recur(start, end, word_dict, explored, limit-1)

def main():
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   word_dict = {}

   # You need to change the pickle file name
   with open("Last_FirstInitial_Lab3.pkl", "rb") as infile:
      word_dict = pickle.load(infile)
   limit = 9
   path_and_steps = (solve(initial, goal, word_dict, limit))
   if path_and_steps != None:
      print ("Path:", path_and_steps[0])
      print ("steps within {} limit:".format(limit), path_and_steps[1])
   else:
      print ("Solution not found in {} steps".format(limit))
   
   # Now, start iterative deepening
   '''Your code goes here'''
   
   # Print out the shortest path and length of the path (number of steps)
   

if __name__ == '__main__':
   main()
