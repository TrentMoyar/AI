import math
import sys
import random

def logistic(x):
   return 1/(1 + math.exp(-x))

#Nodes indexed by integer
class NeuralNet:
   def __init__(self, inputnum):
      inputlayer = {node : [inputnum + 1, inputnum + 2] for node in range(inputnum + 1)}
      hiddenlayer = {inputnum + 1 : [inputnum + 3], inputnum + 2: [inputnum + 3]}
      self.inputnum = inputnum
      self.children = {**inputlayer, **hiddenlayer}
      self.parents = self.get_parents(self.children)
      self.weights = self.get_weights(self.children)
      self.alpha = 0.1
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
            if child < (self.inputnum + 3):
               weights[(parent, child)] = random.normalvariate(0, math.sqrt(2/6))
            else:
               weights[(parent, child)] = random.normalvariate(0, math.sqrt(2/3))
      return weights
   def get_output(self, inputs):
      outputs = inputs + [1]
      for node in range(len(inputs) + 1, len(inputs) + 4):
         parents = self.parents[node]
         value = 0
         for parent in parents:
            value += outputs[parent]*self.weights[(parent, node)]
         outputs.append(logistic(value))
      return outputs[-1]

   def back_propogate(self, inputs, output):
      deltas = [0 for i in range(len(inputs) + 4)]
      outputs = inputs + [1]
      for node in range(len(inputs) + 1, len(inputs) + 4):
         parents = self.parents[node]
         value = 0
         for parent in parents:
            value += outputs[parent]*self.weights[(parent, node)]
         outputs.append(logistic(value))

      deltas[-1] = (output - outputs[-1])*outputs[-1]*(1 - outputs[-1])

      for node in range(len(inputs) + 1, len(inputs) + 3):
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
      for x in range(self.inputnum + 1, self.inputnum + 4):
         temp = []
         for y in self.parents[x]:
            temp.append(self.weights[(y,x)])
         toreturn.append(temp)
      toreturn.append([1])
      return toreturn

   def to_string(self):
      toreturn = "Layer counts: [" + str(self.inputnum + 1) + ", 2, 1, 1]\n"
      toreturn += "Weights: "
      weights = self.format_weights()
      toreturn += '\n' + str(weights[0] + weights[1])
      toreturn += '\n' + str(weights[2])
      toreturn += '\n' + str(weights[3])
      return toreturn

def main():
   file = sys.argv[1]
   testinputs = []
   testoutputs = []
   with open(file) as f:
      inputdata = f.readlines()
      for i in inputdata:
         split = i.split(' => ')
         testinputs.append(list(map(int, split[0].split(' '))))
         testoutputs.append(int(split[1]))
   choices = list(range(len(testinputs)))
   i = 1
   net = NeuralNet(len(testinputs[0]))
   prev = 10000
   while True:
      error = 0
      random.shuffle(choices)
      for choice in choices:
         error += 0.5*(net.back_propogate(testinputs[choice], testoutputs[choice])**2)
      if i % 50000 == 0:
         print(net.to_string())
         if error > 0.3:
            net = NeuralNet(len(testinputs[0]))
      if error < 0.01:
         print(net.to_string())
         break
      prev = error
      i += 1

if __name__ == "__main__":
   main()

'''
Input:
1 0 1 => 1
...
Output:
Layer cts: [3, 2, 1, 1]
Weights:
[0.9070., 1.7216.., 0.7438.., -3.9361.., -3.6020.., 0.7762..]
[1.1885.., -4.5897..]
[1.3842..]
'''