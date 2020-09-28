# Name: Trent Moyar
# Period: 3
# Do not forget to change the file name -> Save as

import string
import os
import itertools
from PIL import Image

'''Day 1 Tasks: '''
# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
l = [int(x) for x in input("list of numbers: ").strip().split()]
print ("1. sum of numbers:",sum(l))

# 2. Output the list of those integers (from #1) that are divisible by three.
print ("2. nums divisible by 3:",[x for x in l if x%3 == 0])


# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8
fib = [1]*int(input("integer for fibonacci: "))
for x in range(2,len(fib)):
   fib[x] = fib[x-1]+fib[x-2]
print("3. fibonacci:",str(fib).strip("[]"))


# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
print ("4. every other character",input("enter a string to alternate: ")[::2])


# 5. Given a positive integer input, check whether the number is prime or not.
prime = int(input("enter a positive int: "))
bool = True
for x in range(2,int((prime**0.5)+1)):
   if(prime%x == 0):
      bool = False
print("5. is it prime:", bool & (prime != 1))

# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
tri = [int(x) for x in input("enter tirangle lengths: ").split()]
print("6. area of triangle:",(sum(tri)*0.5*(sum(tri)*0.5-tri[0])*(sum(tri)*0.5-tri[1])*(sum(tri)*0.5-tri[2]))**0.5)


# 7. Given a input of a string, remove all punctuation from the string. 
punc = "".join([x for x in input("enter a sentence: ") if x in string.ascii_letters])
print ("7. punctuation removed:",punc)

# eg. "Don't quote me," she said. -> Dontquotemeshesaid
# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
punc = punc.lower()
print("8. is palindrome:",punc == punc[::-1])
   

# 9. Count the number of each vowel in the input string (from #7).
vowel = {'a':0,'e':0,'i':0,'o':0,'u':0}
for x in punc:
   if x in vowel:
      vowel[x] += 1
print ("9. number of each vowel:",str(vowel).strip("{}"))

 
# 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.  
# eg. 2 5 -> 0, 2, 6, 12
values = input("enter two ints: ").strip().split()
print("10. output of the function:",[x**2 - 3*x + 2 for x in range(int(values[0]), int(values[-1]) + 1)])



'''Day 2 Tasks: '''

# 11. Given an input of a string, determines a character with the most number of occurrences.
inp = input("enter string: ")
chars = {}
for x in inp:
   chars[x] = 1 if x not in chars else chars[x] + 1
print("11. the most common character is:",sorted(chars.keys(), key=lambda char: chars[char])[-1])

# 12. With the input string from #11, output a list of all the words that start and end in a vowel.
print("12. words that start and end with vowels:",[x for x in inp.split() if (x[0] in vowel) & (x[-1] in vowel)])

# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
print("13. with words capitalized:",inp.title())

# 14. With the input string from #11, prints out the string with each word in the string reversed.
print("14. with words reversed:", " ".join([x[::-1] for x in inp.split()]))
# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest 
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# 	eg.    b Ba baby boy ->  BaaBay Baoy
words = inp.split(" ",maxsplit = 2)
if len(words) > 2:
   print("15. words replaced: ",words[2].replace(words[0], words[1]))
else:
   print("15. can't replace: improper formatting")
 
# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
inp = input("enter string to remove duplicates: ")
print("16. removed duplicates:","".join([x for y,x in enumerate(inp) if x not in inp[0:y]]))


# 17. Given an input of a string, determines whether the string contains only digits.
inp = input("enter string to check the digits: ")
bool = False not in [x.isdigit() for x in inp]
print("17. is only digits:",bool)
# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string, 
# converts it to a number, and prints out the decimal value.
if bool:
   if False not in [x in "01" for x in inp]:
      print("18. binary to decimal:", int(inp,2))
   else:
      print("18. not a binary number")
else:
   print("18. not a number")
 
# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.
print("19. are anagrams:",sorted(input("input a string: ")) == sorted(input("input another string: ")))


# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.
file = input("input an image filename: ")
if not os.path.isfile(file):
   print("20. file doesn't exist")
else:
   print("20. image size:",Image.open(file).size)



''' Challenging Questions: '''

# 21. Given an input of a string, find the longest palindrome within the string.
inp = "".join(input("enter string to find longest palindrome: ").split())
sublist = []
for x in range(0,len(inp)-1):
   for y in range(x+2,len(inp)+1):
      if(inp[x:y] == inp[x:y][::-1]):
         sublist.append(inp[x:y])
print("21. the longest palindrome:",sorted(sublist,key=len)[-1] if len(sublist) > 0 else "no palindrome")

 
# 22. Given an input of a string, find all the permutations of a string.
perm = input("enter string to do permutations: ")
perms = ["".join(x) for x in itertools.permutations(perm,len(perm))]
print("22. all permutations:", perms)
# 23. Given the input string from #22, find all the unique permutations of a string.
print("23. all unique permutations:", set(perms))

# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).
inp = "".join(input("enter string to find longest non-decreasing sequence: ").split())
sublist = []
for x in range(0,len(inp)-1):
   for y in range(x+2,len(inp)+1):
      if(False not in [False for a,b in enumerate(inp[x+1:y]) if ord(b) < ord(inp[x+a])]):
         sublist.append(inp[x:y])
print("24. the longest non-decreasing sequence:",sorted(sublist,key=len)[-1] if len(sublist) > 0 else "no input")

