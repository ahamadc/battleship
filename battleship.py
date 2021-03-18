import random
import os

# setting x, y coordinates of target
x, y = random.randint(1, 8), random.randint(1, 8)

# variables to hold aim coordiantes for each try
a, b = 1, 1

# number of tries to hit target
tries = 0

# limit on the number of tries
limit = 1

# win variable
win = False

# variable to control validity check
valid = False

# battleship board
board = [[' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
         [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
         [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
         [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
         [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
         [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
         [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
         [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],]

# 'press enter' pause
def continu(): input('press enter to continue ')

# default screen clear and title + stats
def clrscrn():
    os.system('cls')
    print('----------\nBATTLESHIP\n----------\n' + 'try:', tries, '\ntries left:', limit - tries, '\n')
    printboard()

# display battleship game board
def printboard():
    for i in board:
        k = ''
        for x in i:
            k += x
        print(k)
    print('\n')        

# play game
while tries < limit:
    # increase number of tries
    tries += 1
    
    clrscrn()
    
    # take inputs for a and b
    a = input('a: ')
    b = input('b: ')
    
    # a and b validity check
    valid = False
    while valid == False:
        # check if a and b are integers
        if a.isdigit() and b.isdigit():
            # check if a and b are within limits
            if int(a) > 8 or int(a) < 1 or int(b) > 8 or int(b) < 1:
                print('a and b must both be between 1 and 8')
                a = input('a: ')
                b = input('b: ')
                continu()
            else:
                a, b = int(a), int(b)
                valid = True
        else:
            print('a and b must be integers')
            a = input('a: ')
            b = input('b: ')
            continu()
    
    #check if the target has been hit
    if a == x and b == y:
        board[a - 1][b - 1] = ' ! '
        win = True
        break
    else:
        board[a - 1][b - 1] = ' X '
    print('\n')
    printboard()
    continu()

# showing target for end scene
board[x - 1][y - 1] = ' ! '

# end scene
if win:
    clrscrn()
    print('YOU WON!')
    continu()
else:
    clrscrn()
    print('YOU LOST :(')
    continu()
    