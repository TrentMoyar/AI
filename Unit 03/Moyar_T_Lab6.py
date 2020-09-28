import sys
import re
import string
import random

BLOCKCHAR = '#'
PROTECTEDCHAR = '~'
OPENCHAR = '-'

CHAR_DICT = {}
WORD_SET = set()
DICTIONARY = {}

ACROSS_REG = "(?<={0})[^{0}]".format(BLOCKCHAR, OPENCHAR)
CHECK_REG = "(?<={0})(?![^{0}]*{1})[^{0}]+(?={0})".format(BLOCKCHAR, OPENCHAR)
THREE_REG = "{0}[^{0}]{{1,2}}{0}".format(BLOCKCHAR)
PRELIM_REG = "{0}({2}{1}|{1}{2}|{1}{1}|{1}){0}".format(BLOCKCHAR,PROTECTEDCHAR,OPENCHAR)
ONEFILL_REG = "(?<={0}){1}(?={0})".format(BLOCKCHAR, OPENCHAR)
TWOFILL_REG = "(?<={0}){1}{1}(?={0})".format(BLOCKCHAR, OPENCHAR)
SIZE_REG = r"^(\d+)x(\d+)$"
WALL_REG = r"^\d+$"
WORD_REG = r"^(H|V)(\d+)x(\d+)(.+)$"
PROTECT_REG = "(?<={0})[{1}{2}]{{3}}(?={0})".format(BLOCKCHAR, PROTECTEDCHAR, OPENCHAR)
LEFT_REG = "(?<={0}){1}[^{0}]{{2}}".format(BLOCKCHAR, PROTECTEDCHAR)
RIGHT_REG = "[^{0}]{{2}}{1}(?={0})".format(BLOCKCHAR,PROTECTEDCHAR)
MID_REG = "(?<={0})(?=[^{0}]*{1})[^{0}]{{3}}(?={0})".format(BLOCKCHAR,PROTECTEDCHAR)
PROTECT_SUB = "{0}{0}{0}".format(PROTECTEDCHAR)
ONE_SUB = "{0}".format(BLOCKCHAR)
TWO_SUB = "{0}{0}".format(BLOCKCHAR)
PREV_ARGS = 4

def get_all_indices(board,width):
   DOWN_REG = "(?<={0}.{{{1}}})[^{0}]".format(BLOCKCHAR,width + 1)
   toreturn = []
   for m in re.finditer(ACROSS_REG,board):
      sindex = m.start()
      lindex = sindex
      while board[lindex] != BLOCKCHAR:
         lindex += 1
      toreturn.append((sindex, lindex, 1,width+2))

   for m in re.finditer(DOWN_REG, board):
      sindex = m.start()
      lindex = sindex
      while board[lindex] != BLOCKCHAR:
         lindex += width + 2
      lindex -= width + 1
      toreturn.append((sindex, lindex, width+2,1))
   return toreturn

def get_indices(board, width):
   DOWN_REG = "(?<={0}.{{{1}}})[^{0}]".format(BLOCKCHAR,width + 1)
   toreturn = []
   for m in re.finditer(ACROSS_REG,board):
      sindex = m.start()
      lindex = sindex
      good_word = False
      while board[lindex] != BLOCKCHAR:
         if board[lindex] == OPENCHAR:
            good_word = True
         lindex += 1
      if good_word:
         toreturn.append((sindex, lindex, 1,width+2))

   for m in re.finditer(DOWN_REG, board):
      sindex = m.start()
      lindex = sindex
      good_word = False
      while board[lindex] != BLOCKCHAR:
         if board[lindex] == OPENCHAR:
            good_word = True
         lindex += width + 2
      lindex -= width + 1
      if good_word:
         toreturn.append((sindex, lindex, width+2,1))
   return toreturn

def get_affected(board, index):
   toreturn = []
   for x in range(index[0], index[1], index[2]):
      while board[x - index[3]] != BLOCKCHAR:
         x -= index[3]
      sindex = x
      while board[x + index[3]] != BLOCKCHAR:
         x += index[3]
      toreturn.append((sindex,x+1,index[3],index[2]))
   return toreturn

def upd_constraints(board, index, constraints):
   toreturn = set()
   for x in range(index[0],index[1], index[2]):
      constraints[x] = set(board[x])
   for ind in get_affected(board,index):
      length = (ind[1] - ind[0] - 1)//ind[2] + 1
      letters = [set() for x in range(length)]
      words = get_gre_words(board, ind)
      for word in words:
         for x in range(length):
            letters[x].add(word[x])
      word = ""
      for x,y in enumerate(range(ind[0], ind[1], ind[2])):
         word = word + board[y]
         if y in constraints:
            constraints[y] &= letters[x]
      if OPENCHAR not in word:
         toreturn.add(word)
   return toreturn

def gen_constraints(board, width):
   constraints = {}
   for index, val in enumerate(board):
      if val == OPENCHAR:
         constraints[index] = set(string.ascii_uppercase)
      elif val != BLOCKCHAR:
         constraints[index] = set(val)
   for index in get_all_indices(board,width):
      length = (index[1] - index[0] - 1)//index[2] + 1
      letters = [set() for x in range(length)]
      words = get_gre_words(board, index)
      for word in words:
         for x in range(length):
            letters[x].add(word[x])
      for x,y in enumerate(range(index[0], index[1], index[2])):
         if y in constraints:
            constraints[y] &= letters[x]
   return constraints

def index_heur(index, constraints):
   toreturn = 0
   for x in range(index[0], index[1], index[2]):
      toreturn += len(constraints[x])
   return toreturn

def compatible_word(index, word, constraints):
   pos = 0
   for x in range(index[0], index[1], index[2]):
      if word[pos] not in constraints[x]:
         return False
   return True

def check_dupes(board, width):
   dupes = set()
   for index in get_all_indices(board, width):
      word = ""
      for x in range(index[0], index[1], index[2]):
         word = word + board[x]
      if word in dupes:
         return True
      if OPENCHAR not in word:
         dupes.add(word)
   return False


def fill_words(board, width, height, done, constraints):
   if check_dupes(board, width):
      return None

   if OPENCHAR not in board:
      return board
   for x in constraints:
      if len(constraints[x]) == 0:
         return None
   indices = sorted(get_indices(board, width), key=lambda index: index_heur(index, constraints) )
   index = indices[0]
   words = sorted(get_words(board, index, constraints), key=lambda word: word_heur(word), reverse=True)
   for word in words:
      if word not in done:
         nuboard = add_word(board,index,word)
         nuconst = {x:constraints[x].copy() for x in constraints}
         otherw = upd_constraints(nuboard, index, nuconst)
         done.add(word)
         nuboard = fill_words(nuboard, width, height, done, nuconst)
         if nuboard != None:
            return nuboard
         done.remove(word)
   return None

def area_fill(index, board, width, height):
   toreturn = 0
   board[index] = BLOCKCHAR
   if board[index + 1] != BLOCKCHAR:
      toreturn += area_fill(index + 1, board, width, height)
   if board[index - 1] != BLOCKCHAR:
      toreturn += area_fill(index - 1, board, width, height)
   if board[index + width + 2] != BLOCKCHAR:
      toreturn += area_fill(index + width + 2, board, width, height)
   if board[index - width - 2] != BLOCKCHAR:
      toreturn += area_fill(index - width - 2, board, width, height)
   return toreturn + 1

def remove_pad(board, width, height):
   if board == None:
      return None
   nuword = ''
   for x in range(height + 2):
      nuword += board[x*(width+2)+1:x*(width+2)+width+1]
   return nuword[width:-width]

def intersect(board, word_board,width, height):
   if board == None or word_board == None:
      return None
   words = list(word_board)
   for x,y in enumerate(board):
      if y == BLOCKCHAR:
            words[x] = y
   words = ''.join(words)
   nuword = ''
   for x in range(height + 2):
      nuword += words[x*(width+2)+1:x*(width+2)+width+1]
   return nuword[width:-width]

def intersect_nc(board, word_board,width, height):
   if board == None or word_board == None:
      return None
   words = list(word_board)
   for x,y in enumerate(board):
      if y == BLOCKCHAR:
            words[x] = y
   words = ''.join(words)
   return words

def transpose(board, width, height):
   toreturn = ""
   for x in range(0,width + 2):
      toreturn += board[x::(width+2)]
   return toreturn

def pre_check(board, width, height):
   if board != board[::-1]:
      return False
   if re.search(PRELIM_REG, board) != None:
      return False
   if re.search(PRELIM_REG, transpose(board, width, height)) != None:
      return False
   if area_fill(find_char(board), list(board) , width, height) != board.count(PROTECTEDCHAR) + board.count(OPENCHAR):
      return False
   return True

def check_board(board, width, height):
   if board != board[::-1]:
      return False
   if re.search(THREE_REG, board) != None:
      return False
   if re.search(THREE_REG, transpose(board, width, height)) != None:
      return False
   return True

def fill_cracks(board, width, height):
   board = re.sub(LEFT_REG, PROTECT_SUB, board)
   board = re.sub(RIGHT_REG, PROTECT_SUB, board)
   board = re.sub(MID_REG, PROTECT_SUB, board)
   board = re.sub(ONEFILL_REG, ONE_SUB, board)
   board = re.sub(TWOFILL_REG, TWO_SUB, board)
   board = transpose(board, width, height)
   board = re.sub(LEFT_REG, PROTECT_SUB, board)
   board = re.sub(RIGHT_REG, PROTECT_SUB, board)
   board = re.sub(MID_REG, PROTECT_SUB, board)
   board = re.sub(ONEFILL_REG, ONE_SUB, board)
   board = re.sub(TWOFILL_REG, TWO_SUB, board)
   board = transpose(board, height, width)
   return board

def split_rows(board, width, height):
   return [board[i*width:i*width + width] for i in range(height)]

def block_heuristic(index, board, width, height):
   temp = index
   up,down,left,right = 0, 0, 0, 0
   while board[index] != BLOCKCHAR:
      index += 1
      right += 1
   index = temp
   while board[index] != BLOCKCHAR:
      index -= 1
      left += 1
   index = temp
   while board[index] != BLOCKCHAR:
      index += width + 2
      down += 1
   index = temp
   while board[index] != BLOCKCHAR:
      index -= width + 2
      up += 1
   return down*up + left*right

def fill_blocks(board,width,height,walls):
   count =  board.count(BLOCKCHAR) - 2*(width + 2) - 2*height
   if walls == count:
      return board
   if walls < count:
      return None
   indices = [i.start() for i in re.finditer(OPENCHAR, board)]
   indices.sort(key=lambda index: block_heuristic(index,board,width,height), reverse = True)
   for x in indices:
      temp = list(board)
      temp[x] = BLOCKCHAR
      temp[len(temp) - 1 - x] = BLOCKCHAR
      temp = ''.join(temp)
      temp = fill_cracks(temp,width, height)
      if pre_check(temp,width,height):
            nuboard = fill_blocks(temp,width,height, walls)
            if nuboard != None and check_board(nuboard, width, height):
               return nuboard
   return None

def get_gre_words(board, index):
   pos = 0
   length = (index[1] - index[0] - 1)//index[2] + 1
   toreturn = DICTIONARY[get_key(pos, board[index[0]],length)].copy()
   for x in range(index[0],index[1],index[2]):
      if board[x] != OPENCHAR:
         toreturn &= DICTIONARY[get_key(pos,board[x],length)]
      pos += 1
   return toreturn

def get_words(board, index, constraints):
   pos = 0
   length = (index[1] - index[0] - 1)//index[2] + 1
   toreturn = DICTIONARY[get_key(pos, board[index[0]],length)].copy()
   pos = 0
   for x in range(index[0],index[1],index[2]):
      s = set()
      for ch in constraints[x]:
         s |= DICTIONARY[get_key(pos, ch, length)]
      pos += 1
      toreturn &= s
   return toreturn

def add_word(board, index, word):
   board = list(board)
   pos = 0
   for x in range(index[0],index[1],index[2]):
      board[x] = word[pos]
      pos += 1
   board = ''.join(board)
   return board

def find_char(board):
   find_prot = board.find(PROTECTEDCHAR)
   if find_prot == -1:
      return board.find(OPENCHAR)
   else:
      return find_prot

def word_heur(word):
   toreturn = 1
   for x in word:
      toreturn *= CHAR_DICT[x]
   return toreturn

def get_key(position, char, length):
   return '{0}{1}{2}'.format(position,char,length)

def main():
   args = sys.argv
   height, width = tuple(map(int,re.findall(SIZE_REG, args[1])[0]))
   walls = int(re.match(WALL_REG, args[2]).group(0))
   word_board = ['-']*height*width
   empty_board = ['-']*height*width
   for x in range(len(args) - PREV_ARGS):
      inp = args[x + PREV_ARGS]
      reg = re.match(WORD_REG, inp, re.I)
      if reg.group(1).lower() == "h":
            for x in range(len(reg.group(4))):
               word_board[x+int(reg.group(3)) + width*int(reg.group(2))] = reg.group(4)[x]
      else:
            for x in range(len(reg.group(4))):
               word_board[x*width+int(reg.group(3)) + width*int(reg.group(2))] = reg.group(4)[x]
   words_string = BLOCKCHAR*(width+3) + (BLOCKCHAR*2).join(split_rows(''.join(word_board), width, height)) + BLOCKCHAR*(width+3)
   empty_board = BLOCKCHAR*(width+3) + (BLOCKCHAR*2).join(split_rows(''.join(empty_board), width, height)) + BLOCKCHAR*(width+3)
   words_string = words_string.upper()
   if walls == height*width:
      empty_board = list(BLOCKCHAR*walls)
   if height*width % 2 == 0 and walls % 2 == 1:
      return
   words_string = list(words_string)
   empty_board = list(empty_board)
   if height*width % 2 == 1 and walls % 2 == 1:
      words_string[int((len(words_string)-1)/2)] = BLOCKCHAR
      empty_board[int((len(words_string)-1)/2)] = BLOCKCHAR
   if height*width % 2 == 1 and walls % 2 == 0:
      empty_board[int((len(words_string)-1)/2)] = PROTECTEDCHAR
   for x,y in enumerate(words_string):
      if y in string.ascii_letters:
            empty_board[x] = PROTECTEDCHAR
      if y == BLOCKCHAR:
            empty_board[x] = BLOCKCHAR
   for x,y in enumerate(words_string[::-1]):
      if y in string.ascii_letters:
            empty_board[x] = PROTECTEDCHAR
      if y == BLOCKCHAR:
            empty_board[x] = BLOCKCHAR
   empty_board = ''.join(empty_board)
   words_string = ''.join(words_string)
   empty_board = fill_cracks(empty_board, width, height)
   empty_board = fill_blocks(empty_board,width,height,walls)
   new_board = intersect_nc(empty_board, words_string, width,height)
   dict_file = args[3]
   words = []
   with open(dict_file) as f:
      words = f.readlines()
   for x in words:
      temp = str.upper(x.strip())
      WORD_SET.add(temp)
      for index, char in enumerate(temp):
            if char in CHAR_DICT:
               CHAR_DICT[char] += 1
            else:
               CHAR_DICT[char] = 1
            key = get_key(index,char,len(temp))
            if key in DICTIONARY:
               DICTIONARY[key].add(temp)
            else:
               DICTIONARY[key] = set([temp])
            key = get_key(index, OPENCHAR, len(temp))
            if key in DICTIONARY:
               DICTIONARY[key].add(temp)
            else:
               DICTIONARY[key] = set([temp])
   done = set()
   for index in get_all_indices(new_board, width):
      word = []
      for x in range(index[0], index[1], index[2]):
         word.append(new_board[x])
      if OPENCHAR not in word:
         done.add(''.join(word))
   constraints = gen_constraints(new_board, width)
   print(remove_pad(fill_words(new_board,width, height,done, constraints),width, height))

if __name__ == "__main__":
   main()