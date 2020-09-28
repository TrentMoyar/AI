# Name:          Date:
import heapq
import random, time, math

class PriorityQueue():
   # copy your PriorityQueue() from Lab5
   # If you need any method(s), add them.
   pass

def inversion_count(new_state, size):
   ''' Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   # Your code goes here
   return True
   
def check_inversion():
   t1 = inversion_count("_42135678", 3)
   f1 = inversion_count("21345678_", 3)
   return t1 and not f1

def getInitialState(sample):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   if(inversion_count(new_state, 3)): return new_state
   else: return None
   
def swap(n, i, j):
   # Your code goes here
   return n
      
def generateChild(n, size):
   # Your code goes here
   return []

def display_path(path_list, size):
   for n in range(size):
      for i in range(len(path_list)):
         print (path_list[i][n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

def dist_heuristic(start, goal, size):
   # Your code goes here
   return 0

def a_star(start, goal="_12345678", heuristic=dist_heuristic):
   frontier = PriorityQueue()
   if start == goal: return []
   size = 3
   # Your code goes here
   return None

def main():
    # A star
   print ("Inversion works?:", check_inversion())
#    initial_state = getInitialState("_12345678")
#    while initial_state == None:
#       initial_state = getInitialState("_12345678")
   initial_state = input("Type initial state: ")
   cur_time = time.time()
   path = (a_star(initial_state))
   if path != None: display_path(path, 3)
   else: print ("No Path Found.")
   print ("Duration: ", (time.time() - cur_time))

if __name__ == '__main__':
   main()

''' Sample output 1:

Inversion works?: True
Type initial state: 76423_581
764   764   764   764   764   _64   6_4   64_   641   641   641   641   641   _41   4_1   431   431   431   431   _31   3_1   31_   312   312   312   _12   
23_   231   231   2_1   _21   721   721   721   72_   7_2   732   732   _32   632   632   6_2   652   652   _52   452   452   452   45_   4_5   _45   345   
581   58_   5_8   538   538   538   538   538   538   538   5_8   _58   758   758   758   758   7_8   _78   678   678   678   678   678   678   678   678   

The shortest path length is : 26
Duration:  0.06485509872436523


Sample output 2:

Inversion works?: True
Type initial state: 84765231_
847   847   847   847   _47   4_7   47_   472   472   472   472   472   472   472   472   472   472   472   472   472   472   4_2   _42   142   142   142   142   1_2   _12   
652   652   6_2   _62   862   862   862   86_   861   861   8_1   _81   381   381   3_1   31_   315   315   315   _15   1_5   175   175   _75   375   375   3_5   345   345   
31_   3_1   351   351   351   351   351   351   35_   3_5   365   365   _65   6_5   685   685   68_   6_8   _68   368   368   368   368   368   _68   6_8   678   678   678   

The shortest path length is : 29
Duration:  0.28726887702941895

'''
