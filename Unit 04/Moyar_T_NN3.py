import math
import sys
import random
import re

def logistic(x):
   if x < 0:
      return 1 - 1/(1 + math.exp(x))
   else:
      return 1/(1 + math.exp(-x))

#Nodes indexed by integer, nodenums in format [l1, l2, l3]
class NeuralNet:
   
   def __init__(self, nodenums):
      self.indices = []
      prev = 0
      self.nodenums = nodenums
      for x in nodenums:
         self.indices.append(list(range(prev, prev + x)))
         prev = prev + x
      #inputlayer = {node : [inputnum + 1, inputnum + 2, inputnum + 3] for node in range(inputnum + 1)}
      #hiddenlayer = {inputnum + 1 : [inputnum + 4], inputnum + 2: [inputnum + 4], inputnum + 3: [inputnum + 4]}
      self.children = self.get_children()
      self.parents = self.get_parents(self.children)
      self.weights = self.get_weights(self.children)
      self.alpha = 0.1
   def get_children(self):
      children = {}
      for x in range(len(self.indices) - 1):
         for y in self.indices[x]:
            children[y] = self.indices[x + 1]
      return children
   def get_parents(self, children):
      parents = {}
      for parent in children:
         for child in children[parent]:
            if child not in parents:
               parents[child] = []
            parents[child].append(parent)
      return parents
   def get_weights(self, children):
      weights = {}
      for parent in children:
         for child in children[parent]:
            fanin = 0
            fanout = 0
            for layer in self.indices:
               if child in layer:
                  fanout = len(layer)
               if parent in layer:
                  fanin = len(layer)
            weights[(parent, child)] = random.normalvariate(0, math.sqrt(2/(fanin + fanout)))
      return weights
   def get_output(self, inputs):
      outputs = inputs + [1]
      for node in range(len(inputs) + 1, len(inputs) + 5):
         parents = self.parents[node]
         value = 0
         for parent in parents:
            value += outputs[parent]*self.weights[(parent, node)]
         outputs.append(logistic(value))
      return outputs[-1]

   def back_propogate(self, inputs, output):
      deltas = [0 for i in range(self.indices[-1][-1] + 1)]
      outputs = inputs + [1]
      for node in range(self.indices[1][0], self.indices[-1][-1]+1):
         parents = self.parents[node]
         value = 0
         for parent in parents:
            value += outputs[parent]*self.weights[(parent, node)]
         outputs.append(logistic(value))

      deltas[-1] = (output - outputs[-1])*outputs[-1]*(1 - outputs[-1])

      for layer in self.indices[:-1][::-1]:
         for node in layer:
            value = 0
            for child in self.children[node]:
               value += self.weights[(node, child)]*deltas[child]
            value = value*outputs[node]*(1 - outputs[node])
            deltas[node] = value
      for weight in self.weights:
         self.weights[weight] = self.weights[weight] + self.alpha * deltas[weight[1]] * outputs[weight[0]]
      return output - outputs[-1]

   def format_weights(self):
      toreturn = []
      for y in self.indices[1:]:
         layer = []
         for x in y:
            temp = []
            for y in self.parents[x]:
               temp.append(self.weights[(y,x)])
            layer.append(temp)
         toreturn.append(layer)
      toreturn.append([[1]])
      return toreturn

   def to_string(self):
      toreturn = "Layer counts: " + str(self.nodenums)[:-1] + ", 1]\n"
      toreturn += "Weights: "
      weights = self.format_weights()
      for layer in weights:
         toreturn += str(layer) + '\n'
      return toreturn

def inequality(first, second, inequal):
   if inequal == '<=':
      return first <= second
   if inequal == '>=':
      return first >= second
   if inequal == '<':
      return first < second
   if inequal == '>':
      return first > second

def main():
   inequal = re.search(r'[<>=]+', sys.argv[1]).group()
   number = float(re.search(r'[.\d]+', sys.argv[1]).group())
   i = 1
   net = NeuralNet([3, 14, 3, 1])
   prev = 10000
   outradius = 1000
   inradius = number
   while True:
      error = 0
      testinput = [random.uniform(-outradius,outradius),random.uniform(-outradius,outradius)]
      output = int(inequality(testinput[0]**2 + testinput[1]**2, number, inequal))
      error += 0.5*(net.back_propogate(testinput, output)**2)
      testinput = [random.uniform(-inradius,inradius),random.uniform(-inradius,inradius)]
      output = int(inequality(testinput[0]**2 + testinput[1]**2, number, inequal))
      error += 0.5*(net.back_propogate(testinput, output)**2)
      if error < 0.01:
         net.alpha = 0.01
      if error < 0.001:
         net.alpha = 0.001
      if i % 10000 == 0:
         print(net.to_string())
      i += 1

if __name__ == "__main__":
   main()

'''
Input:
1 0 1 => 1

Output:
Layer cts: [3, 2, 1, 1]
Weights:
[0.9070., 1.7216.., 0.7438.., -3.9361.., -3.6020.., 0.7762..]
[1.1885.., -4.5897..]
[1.3842..]
'''