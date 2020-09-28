#Trent Moyar
#1/16/2020

import sys

def main():
   idx = int(sys.argv[1]) - 30
   myRegexList = [
      r"/^0$|^10[01]$/",
      r"/^[01]*$/",
      r"/^\d*0$/",
      r"/\b\w*[aeiou]\w*[aeiou]\w*\b/i",
      r"/^0$|^1[01]*0$/",
      r"/^[01]*110[01]*$/",
      r"/^.{2,4}$/s",
      r"/^\d{3}\s*-?\s*\d{2}\s*-?\s*\d{4}$/",
      r"/^.*?d\w*\b/mi",
      r"/^[01]?$|^0[01]*0$|^1[01]*1$/",
   ]
   print(myRegexList[idx])

if __name__ =='__main__':
   main()