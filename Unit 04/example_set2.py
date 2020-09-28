import math

def g(x):
   return 1.0/(1.0 + math.exp(-x))

def one(one, two, three, four):
   summ = one*1.35 + two*-1.34 + three*-1.66 + four*-0.55
   print(1, g(summ))
   return g(summ)

def two(one, two, three, four):
   summ = one*-0.9 + two*-0.58 + three*-1.0 + four*1.78
   print(2, g(summ))
   return g(summ)

def three(one, two):
   summ = one*-1.08 + two*-0.7
   print(3, g(summ))
   return g(summ)

pval = three(one(1,0,1,1), two(1,0,1,1))
print(1 - pval*-0.6)