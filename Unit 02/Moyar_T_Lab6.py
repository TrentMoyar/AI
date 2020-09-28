#Trent Moyar
#Period 3
import math, random

weight_dict = {}
def scale(board, N):
   global weight_dict
   greatest = int((N-1)*N/2)
   represent = tuple(board)
   if represent in weight_dict:
      return weight_dict[represent]
   diag1 = [0 for x in range(N*2 - 1)]
   diag2 = [0 for x in range(N*2 - 1)]
   rows = [0 for x in range(N)]
   cols = [0 for x in range(N)]
   summ = 0
   for x in range(N):
      ri = board[x]
      ci = x
      summ += cols[ci]
      cols[ci] += 1
      summ += rows[ri]
      rows[ri] += 1
      summ += diag1[ri + ci]
      diag1[ri + ci] += 1
      summ += diag2[ri - ci + (N - 1)]
      diag2[ri - ci + (N - 1)] += 1
   weight_dict[tuple(board)] = (greatest - summ)
   return (greatest - summ)
def random_board(N):
   nums = list(range(N))
   return random.sample(nums,N)
def solve(N):
   SIZE = 2000
   GOAL = int((N-1)*N/2)
   population = [random_board(N) for x in range(SIZE)]
   weights = []
   for x in range(SIZE):
      weight = scale(population[x],N)
      if weight == GOAL:
         return population[x]
      weights.append(weight)
   a = 0
   while True:
      print(a)
      a += 1
      new_population = []
      new_weights = []
      choices = random.choices(population,weights=weights,k=(SIZE))
      count = 0
      for x in range(SIZE//2):
         x1 = choices[count]
         x2 = choices[count + 1]
         count += 2
         child1,child2 = reproduce(x1,x2,N)
         mutate_prob = random.random()
         if mutate_prob < 0.9:
            child1 = mutate(child1,N)
         weight = scale(child1,N)
         if weight == GOAL:
            return child1
         new_population.append(child1)
         new_weights.append(weight)
         mutate_prob = random.random()
         if mutate_prob < 0.9:
            child2 = mutate(child2,N)
         weight = scale(child2,N)
         if weight == GOAL:
            return child2
         new_population.append(child2)
         new_weights.append(weight)
      population = new_population
      weights = new_weights
   return None
def mutate(board,N):
   toreturn = board[:]
   first = random.randrange(0,N)
   second = random.randint(first,N)
   for x in range(first,second):
      toreturn[x] = random.randrange(0,N)
   return toreturn
def reproduce(x1,x2,N):
   split = random.randrange(0,N)
   child1 = x1[0:split] + x2[split:N]
   child2 = x2[0:split] + x1[split:N]
   return child1, child2
def display(board, N):
   board_matrix = [[0 for x in range(N)] for y in range(N)]
   for x in range(N):
      board_matrix[board[x]][x] = 1
   for x in board_matrix:
      print(x)

def main():
   N = int(input("Enter N: "))
   solution = solve(N)
   display(solution,N)
if __name__ == '__main__':
   main()