#Name: Trent Moyar
#Date: 9/12/2019

class tokenize:
   def __init__(self, text):
      self.text = text.split(" ")
      self.negative = 1
      self.table = {'X': (5, 'X'), 'P': (4, 'X^2'), 'C':(3, 'X^3'), 'PP': (2, 'X^4'), 'PC': (1, 'X^5'), 'CC': (0, 'X^6'), 'U':(6,'')}
   def next(self):
      next = self.text.pop(0)
      while next == 'M':
         self.negative *= -1
         next = self.text.pop(0)
      return (self.table[next[0:-1]], int(next[-1])*self.negative)
   def hasnext(self):
      return len(self.text) != 0
      
def main():
   tokenizer = tokenize(input("Type an expression: "))
   toreturn = []
   while tokenizer.hasnext():
      toreturn.append(tokenizer.next())
   s = ""
   for x in sorted(toreturn, key= lambda val: val[0][0]):
      if x[1] < 0:
         s += ' - ' +  str(abs(x[1])) + x[0][1]
      else:
         s += ' + ' + str(abs(x[1])) + x[0][1]
   if s[1] == '-':
      s = s[3:]
      s = '-' + s
   else:
      s = s[3:]
   print(s)

if __name__ == '__main__':
   main()