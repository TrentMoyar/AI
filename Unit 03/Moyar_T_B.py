#Trent Moyar
#1/23/2020

import sys

def main():
   idx = int(sys.argv[1]) - 40
   myRegexList = [
      r"/^[x.o]{64}$/i",
      r"/^[xo]*\.[xo]*$/i",
      r"/^(\..*|.*\.|x+o*\..*|.*\.o*x+)$/i",
      r"/^(..)*.$/s",
      r"/^(0([01]{2})*|1([01]{2})*[01])$/",
      r"/\b\w*((a[eiou])|(e[aiou])|(i[eaou])|(o[eiau])|(u[eioa]))\w*\b/i",
      r"/^(1?0)*1*$/",
      r"/^[bc]*[abc][bc]*$/",
      r"/^((([bc]*a){2})+[bc]*|[bc]+)$/",
      r"/^(2(([02]*1){2})*|1(([02]*1){2})*[02]*1)[02]*$/"
   ]
   print(myRegexList[idx])

if __name__ =='__main__':
   main()
  