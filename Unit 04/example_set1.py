import math

def g(x):
   return 1/(1 + math.exp(-x))

def six(one, two, three, four, five):
   summ = one*5 + two*8 + three*2 + four*0 + five*1
   return g(summ)

def seven(one, two, three, four, five):
   summ = one*2 + two*2 + three*2 + four*3 + five*7
   return g(summ)

def eight(one, two, three, four, five):
   summ = one*5 + two*4 + three*4 + four*3 + five*2
   return g(summ)

def nine(six, seven, eight):
   summ = six*0 + seven*1 + eight*7
   return g(summ)

def ten(six, seven, eight):
   summ = six*5 + seven*4 + eight*3
   return g(summ)

nines = nine(six(5,2,3,1,4), seven(5,2,3,1,4), eight(5,2,3,1,4))
tens = ten(six(5,2,3,1,4), seven(5,2,3,1,4), eight(5,2,3,1,4))

print(nines*0.5, tens*-1)