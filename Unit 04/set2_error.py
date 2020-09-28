import math

def g(x):
   return 1.0/(1.0 + math.exp(-x))

def one(one, two, three, four):
   summ = one*1.3522 + two*-1.34 + three*-1.6578 + four*-0.5478
   print(1, g(summ))
   return g(summ)

def two(one, two, three, four):
   summ = one*-0.8983 + two*-0.58 + three*-0.9983 + four*1.7817
   print(2, g(summ))
   return g(summ)

def three(one, two):
   summ = one*-1.083 + two*-0.7046
   print(3, g(summ))
   return g(summ)

pval = three(one(1,0,1,1), two(1,0,1,1))
print(0.5*(1- pval*-0.5751)**2)