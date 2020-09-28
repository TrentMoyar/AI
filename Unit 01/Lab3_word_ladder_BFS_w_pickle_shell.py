# This is the correct shell code for Word Ladder BFS
import pickle

''' Node class or helper methods '''

# you can modify this method or not using it
def generate_path(current, explored):
   list = [current]
   count = 0
   while explored[current] != "":       #assume the parent of root is ""
      list.append(explored[current])
      current = explored[current]
      count += 1
   return (list[::-1], count+1)

# you can change the arguments
def solve(start, end, word_dict):
   ''' you can modify this method '''
   explored = {start:""}
   return (["No solution"], 0)

def main():
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   word_dict = {}
   with open("Moyar_T_Lab3.pkl", "rb") as infile:
      word_dict = pickle.load(infile)
   print (solve(initial, goal, word_dict))

if __name__ == '__main__':
   main()
