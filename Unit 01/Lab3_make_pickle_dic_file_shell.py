import pickle
import string

def generate_adjacents(current, word_list):
   adj_list = set()
   ''' Your code goes here '''
   for x in range(len(current)):
      for y in string.ascii_lowercase:
         if (current[x] != y) & (replace(current,x,y) in word_list):
            adj_list.add(replace(current,x,y))
   return adj_list

def replace(state, index, ch):
   '''your code goes here'''
   l = list(state)
   l[index] = ch
   return "".join(l)
   
def main():
   # fill the word_list
   word_list = []
   file = open("words.txt", "r")
   for word in file.readlines():
      word_list.append(word.rstrip('\n'))
   file.close()
   word_dict = {}
   for word in word_list:
      word_dict[word] = generate_adjacents(word, word_list)

   # Save the pickle file
   with open("Moyar_T_Lab3.pkl", "wb") as outfile:
      pickle.dump(word_dict, outfile, protocol = pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
   main()
