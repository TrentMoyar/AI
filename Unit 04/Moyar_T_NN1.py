import math
import sys

def dot_product(list_one, list_two):
   summ = 0
   for x in range(len(list_one)):
      summ += list_one[x]*list_two[x]
   return summ

def hadamard(list_one, list_two):
   length = len(list_one)
   toreturn = []
   for x in range(length):
      toreturn.append(list_one[x] * list_two[x])
   return toreturn


def split_list(l, div):
   toreturn = []
   for x in range(0,len(l),div):
      toreturn.append(l[x:x+div])
   return toreturn

def split_weights(weights):
   toreturn = []
   lengths = []
   for w in weights:
      lengths.append(len(w))
   div = 1
   right_l = []
   for x in lengths[::-1]:
      right_l.insert(0, int(x/div))
      div = int(x/div)
   count = 0
   for x in right_l:
      weights[count] = split_list(weights[count], x)
      count += 1
   return weights

def get_weights(file):
   with open(file) as f:
      strings = f.read().strip().split('\n')
      integers = []
      for s in strings:
         s = s.strip()
         integers.append(list(map(float, s.split(' '))))
      return integers
   return None

def linear(x):
   return x

def ramp(x):
   return x if x > 0 else 0

def logistic(x):
   return 1/(1 + math.exp(-x))

def sigmoid(x):
   return -1 + 2/(1 + math.exp(-x))

functions = [linear, ramp, logistic, sigmoid]

def main():
   g = functions[int(sys.argv[2][1]) - 1]
   weights = get_weights(sys.argv[1])
   model = split_weights(weights)
   toreturn = list(map(float,sys.argv[3:]))
   for layer in model[:-1]:
      temp = []
      for node in layer:
         temp.append(g(dot_product(toreturn,node)))
      toreturn = temp
   print(hadamard(toreturn, model[-1][0]))



if __name__ == "__main__":
   main()
