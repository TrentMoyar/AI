# Change the file name as LastName_FirstName.py
# Submit your file to Google Classroom Python Contest 1
# Name:
# Period:
import sys
def problem_1(input_str):
   # return: a set of lowercase or punctuation characters except a space 
   # Return duplicated chars from the input_str
   # hello world, Helen  -----> {'o', 'e', 'h', 'l'} # the order does not matter
   return set()

def problem_2(input_str):
   # return: a boolean value, True or False
   # Return if two given words as lowercase are anagrams of each other
   # Listen silent -----> True
   # Save vases -----> False
   # stressed dessertt -----> False
   return True

def problem_3(input_str):
   # return: a string
   # Return the output string by making each word in reverse order
   # Java in VA -----> avaj ni av
   return ""

def problem_4(input_str):
   # return: an integer
   # Return the number of vowels (a, e, i, o, u) of a given string
   # Happy Thanksgiving! -----> 4
   return 0

def problem_5(input_str):
   # return: a set of strings
   # Return a set of all permutations of the given string (a 3-distinct-character-long word)
   # You may make a helper method. You are not allowed to import any library
   # xyz -----> {"xyz", "yzx", "zxy", "xzy", "yxz", "zyx"}
   return set()

def problem_6(input_str):
   # return: an integer
   # Return the factorial of the given number (a string type)
   # 4 -----> 24
   # 0 -----> 1
   # -1 -----> 1
   num = int(input_str)
   return 0

def problem_7(input_str):
   # return: an integer
   # Return the sum of digits of the given number (a string type)
   # 1302 -----> 6
   # 234 -----> 9
   return 0

def problem_8(input_str):
   # return: an integer
   # Return the N-th term of Fibonacci sequence
   # 2 -----> 1
   # 6 -----> 8
   N = int(input_str)
   return 0

def problem_9(input_str):
   # return: an integer
   # Return the number of words of the given string
   # How are you? -----> 3
   return 0

def problem_10(input_str):
   # return: a string
   # Return a string composed of every other character starting from index 1
   # programming -----> rgamn
   # How are you? -----> o aeyu
   return ""

def problem_11(input_str):
   # return: a string
   # Return the string which removes all duplicate characters from the given string (a word)
   # hello -----> helo
   # Adam -----> Adm
   return ""

def problem_12(input_str):
   # return: a string
   # Return the second last character of the given string
   # Virginia -----> i
   # a -----> a
   return ""

def problem_13(input_str):
   # return: a boolean
   # Return if the given string, in lower cases, is palindrome or not
   # Anna -----> True
   # I did, did I? -----> False      # do not ignore punctuations
   # Top spot -----> True       # Ignore blanks
   return True

def problem_14(input_str):
   # return: a string
   # Return "odd" if the given number is an odd number
   # Return "even" if the given number is an even number
   # 23 -----> odd
   # 132452 -----> even
   return "odd"

def problem_15(input_str):
   # return: a set
   # Return a set of all divisor of the given number
   # 24 -----> {1, 2, 3, 4, 6, 8, 12, 24}
   # 3 -----> {1, 3}
   number = int(input_str)
   return set()

def problem_16(input_str):
   # return: a string
   # Return a date string (mm/dd/yyyy) by converting the given date string (day-month-year)
   # 9-12-2020 -----> 12/09/2020
   # 23-4-02 -----> 04/23/2002
   return ""

def problem_17(input_str):
   # return: an integer
   # Return the year that the person will turn 100 years old.
   # Given string is consist of the name and the current age of a person.
   # Anna Treehouse 31 -----> 2088
   # Jacob B. Learns 9 -----> 2110
   return 0

def problem_18(input_str):
   # return: a string
   # Return the string with positive numbers (one space btwn numbers)
   # "3 -1 0 44 -21" -----> "3 44"
   return ""

def problem_19(input_str):
   # return: a dictionary
   # Return the dictionary with key = character (lower case, ignore spaces) and value = the number of occurance
   # Hello world! -----> {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1, '!':1}
   return {}

def problem_20(input_str):
   # return: a string
   # Return the winner ('O', 'X', or 'Cat') of the Tic Tac Toe game result from the given input
   # . represents an empty spot. The board is a 9 character string
   # OX.XO.XOO represents OX_ , thus the winner is 'O'
   #                      XO_
   #                      XOO
   # OX.XO.XOO -----> 'O'
   # OXXXOOXOX -----> 'Cat'
   return "Cat"

def problem_21(input_str):
   # return: a string
   # Re-arrange names in alphabetical order of first names and return the string
   # Lisa Garret Bill Aiden Mary -----> Aiden Bill Garret Lisa Mary 
   return ""

def problem_22(input_str):
   # return: a string
   # Return "__ minutes __ seconds" by converting the given total seconds
   # 312 -----> 6 minutes 12 seconds
   seconds = int(input_str)
   return "0 minutes 0 seconds"

def problem_23(input_str):
   # return: an integer
   # Return the total number of legs of all farm animals.
   # chickens = 2 lengs, cows = 4 legs, and pigs = 4 legs
   # The input_str includes the number of chickens, cows, and pigs repectively.
   # 3 4 5 -----> 42
   return 0

def problem_24(input_str):
   # return: an integer
   # Return the sum of ascii code of each character of the given string (ignore spaces)
   # magic -----> 513
   # A bc -----> 262
   return 0

def problem_25(input_str):
   # return: an integer
   # Return the sum of all numbers (separated by a space) except teens (13 through 19)
   # 1 2 3 -----> 6
   # 2 13 1 -----> 3
   return 0

def problem_26(input_str):
   # return: a boolean
   # Return True if the given string contains a X next to a X somewhere.
   # AXXX -----> True
   # AXBX -----> False
   # ABC -----> False 
   return True

def problem_27(input_str):
   # return: an integer
   # Return the difference between the largest and smallest values in numbers in the given string (separated by a space)
   # 10 3 5 6 -----> 7
   # 7 -2 10 -----> 12
   return 0

def problem_28(input_str):
   # return: an integer
   # Return the length of the given string
   # How are you? -----> 12
   # Hello -----> 5
   return 0

def problem_29(input_str):
   # return: a string
   # Return the last character of the given string
   # How are you? -----> ?
   # Hello -----> o
   return ""

def problem_30(input_str):
   # return: a string
   # Given two even length words, separated by a space, create a new word 
   # by combining the first half of the first word and the second half of the second word
   # WooHoo Zoozoo -----> Woozoo
   # HelloThere TheyHere -----> HelloHere
   return ""

def main():
   # All test cases are in text.txt file
   # Each line includes: testNum and input(s) by one space
   # Example: 1 hello world
   # All contest functions are return methods. 
   # Default return is an empty string for unsolved problems.
   outfile = open("submission.txt", "w")
   sys.stdout = outfile
   with open("test.txt") as infile:
      cases = infile.readlines()
      for ind, case in enumerate(cases):
         line = case.strip().split(" ", 1)
         if line[0] == '1': print(ind, problem_1(line[1]))
         elif line[0] == '2': print(ind, problem_2(line[1]))
         elif line[0] == '3': print(ind, problem_3(line[1]))
         elif line[0] == '4': print(ind, problem_4(line[1]))
         elif line[0] == '5': print(ind, problem_5(line[1]))
         elif line[0] == '6': print(ind, problem_6(line[1]))
         elif line[0] == '7': print(ind, problem_7(line[1]))
         elif line[0] == '8': print(ind, problem_8(line[1]))
         elif line[0] == '9': print(ind, problem_9(line[1]))
         elif line[0] == '10': print(ind, problem_10(line[1]))
         elif line[0] == '11': print(ind, problem_11(line[1]))
         elif line[0] == '12': print(ind, problem_12(line[1]))
         elif line[0] == '13': print(ind, problem_13(line[1]))
         elif line[0] == '14': print(ind, problem_14(line[1]))
         elif line[0] == '15': print(ind, problem_15(line[1]))
         elif line[0] == '16': print(ind, problem_16(line[1]))
         elif line[0] == '17': print(ind, problem_17(line[1]))
         elif line[0] == '18': print(ind, problem_18(line[1]))
         elif line[0] == '19': print(ind, problem_19(line[1]))
         elif line[0] == '20': print(ind, problem_20(line[1]))
         elif line[0] == '21': print(ind, problem_21(line[1]))
         elif line[0] == '22': print(ind, problem_22(line[1]))
         elif line[0] == '23': print(ind, problem_23(line[1]))
         elif line[0] == '24': print(ind, problem_24(line[1]))
         elif line[0] == '25': print(ind, problem_25(line[1]))
         elif line[0] == '26': print(ind, problem_26(line[1]))
         elif line[0] == '27': print(ind, problem_27(line[1]))
         elif line[0] == '28': print(ind, problem_28(line[1]))
         elif line[0] == '29': print(ind, problem_29(line[1]))
         elif line[0] == '30': print(ind, problem_30(line[1]))

if __name__ == "__main__": main()