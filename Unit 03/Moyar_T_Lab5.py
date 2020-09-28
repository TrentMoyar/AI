import sys
import re
import string
import random

BLOCKCHAR = '#'
PROTECTEDCHAR = '~'
OPENCHAR = '-'

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
PROTECT_SUB = "{0}{0}{0}".format(PROTECTEDCHAR)
ONE_SUB = "{0}".format(BLOCKCHAR)
TWO_SUB = "{0}{0}".format(BLOCKCHAR)

PREV_ARGS = 4

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
    board = re.sub(ONEFILL_REG, ONE_SUB, board)
    board = re.sub(TWOFILL_REG, TWO_SUB, board)
    board = transpose(board, width, height)
    board = re.sub(LEFT_REG, PROTECT_SUB, board)
    board = re.sub(RIGHT_REG, PROTECT_SUB, board)
    board = re.sub(ONEFILL_REG, ONE_SUB, board)
    board = re.sub(TWOFILL_REG, TWO_SUB, board)
    board = transpose(board, height, width)
    return board

def split_rows(board, width, height):
    return [board[i*width:i*width + width] for i in range(height)]

def fill_blocks(board,width,height,walls):
    count =  board.count(BLOCKCHAR) - 2*(width + 2) - 2*height
    if walls == count:
        return board
    if walls < count:
        return None
    indices = [i.start() for i in re.finditer(OPENCHAR, board)]
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

def find_char(board):
    find_prot = board.find(PROTECTEDCHAR)
    if find_prot == -1:
        return board.find(OPENCHAR)
    else:
        return find_prot

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
    if walls == 0:
        print(intersect(empty_board, words_string, width, height))
        return
    if walls == height*width:
        print(BLOCKCHAR*walls)
        return
    if height*width % 2 == 0 and walls % 2 == 1:
        print(None)
        return
    words_string = list(words_string)
    empty_board = list(empty_board)
    if height*width % 2 == 1 and walls % 2 == 1:
        words_string[int((len(words_string)-1)/2)] = BLOCKCHAR
        empty_board[int((len(words_string)-1)/2)] = BLOCKCHAR
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
    #walls -= empty_board.count(BLOCKCHAR) - 2*(width +2) - 2*height
    empty_board = fill_blocks(empty_board,width,height,walls)
    print(intersect(empty_board, words_string, width,height))



if __name__ == "__main__":
    main()