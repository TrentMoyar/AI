import itertools

def main():
   numbers = list(map(int, input("Enter the numbers: ").split(' ')))
   answer = int(input("Enter the answer: "))
   if len(numbers) > 5:
      perms = [numbers]
   else:
      perms = list(itertools.permutations(numbers))
   newnums = set()
   for perm in perms:
      recurred = recur(perm)
      newnums |= set(recurred)
   for x in newnums:
      if x[0] == answer:
         print(x[1])

def add(num1, num2):
   return num1 + num2
add.__name__ = ' + '
def subtract(num1, num2):
   return num1 - num2
subtract.__name__ = ' - '
def divide(num1, num2):
   return num1 / num2
divide.__name__ = ' / '
def multiply(num1, num2):
   return num1 * num2
multiply.__name__ = ' * '
operators = [add, subtract, multiply, divide]
reverse = {multiply:divide, divide:multiply, add:subtract, subtract:add}

#returns (list of tuples, first value is answer, next is string)
def recur(numbers):
   toreturn = []
   if len(numbers) == 1:
      return [(numbers[0], str(numbers[0]))]
   for index in range(1,len(numbers)):
      temp1 = recur(numbers[0:index])
      temp2 = recur(numbers[index:])
      for firstval in temp1:
         for secval in temp2:
            for operator in operators:
               if secval[0] == 0 and operator == divide:
                  break
               evaluated = operator(firstval[0], secval[0])
               string = '(' + firstval[1] + operator.__name__ + secval[1] + ')'
               toreturn.append((evaluated,string))
   return toreturn

if __name__ == "__main__":
   main()
