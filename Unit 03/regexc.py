#Trent Moyar
#2/3/2020

import sys

def main():
   idx = int(sys.argv[1]) - 50
   myRegexList = [
      r"/(\w)+\w*\1\w*/i",
      r"/\b\w*(\w)(\w*\1){3}\w*\b/i",
      r"/^(0|1)([01]*\1)?$/",
      r"/\b(?=\w*cat)\w{6}\b/i",
      r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i",
      r"/\b(?!\w*cat)\w{6}\b/i",
      r"/\b(?!(\w)+\w*\1)\w+\b/i",
      r"/^(?!.*10011)[01]*$/",
      r"/\w*([aeiou])(?!\1)[aeiou]\w*/i",
      r"/^(?!.*1.1)[01]*$/"
   ]    
   print(myRegexList[idx])

if __name__ =='__main__':
   main()