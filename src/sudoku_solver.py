# This program solves 4x4 sudoku puzzles
# A 4x4 sudoku puzzle has the following form:
#       
# a1 a2 | a3 a4
# b1 b2 | b3 b4
# -------------      
# c1 c2 | c3 c4
# d1 d2 | d3 d4
#
# Where an, bn, cn, dn represent numbers
# ranging in value from 1 to 4. Rows span 
# 4 consecutive numbers horizontally, 
# columns span 4 consecutive numbers 
# vertically, and the 4 squares contain 4
# each. They are visualized above.
# Each row, column, and square may only
# contain one instance of each number
# meaning no duplicates of a number are 
# allowed to be present in a single row,
# column, or square.

from random import shuffle
# random library pseudorandomly generates random values.
# shuffle(x) function: "Shuffle list x in place, and return None."

def instructions():
    print('''This program solves 4x4 sudoku puzzles
A 4x4 sudoku puzzle has the following form:
    
a1 a2 | a3 a4
b1 b2 | b3 b4
-------------      
c1 c2 | c3 c4
d1 d2 | d3 d4

Where an, bn, cn, dn represent numbers
ranging in value from 1 to 4. Rows span 
4 consecutive numbers horizontally, 
columns span 4 consecutive numbers 
vertically, and the 4 squares contain 4
each. They are visualized above.
Each row, column, and square may only
contain one instance of each number
meaning no duplicates of a number are 
allowed to be present in a single row,
column, or square.''')
    
instructions()
# print instructions to user

temp_board = {}
# initialize temporary board variable

all_blocks = {'a1': ' ','a2': ' ','a3': ' ','a4': ' ','b1': ' ','b2': ' ','b3': ' ','b4': ' ','c1': ' ','c2': ' ','c3': ' ','c4': ' ','d1': ' ','d2': ' ','d3': ' ','d4': ' '}
# initialize board with all values initially blanks

unfilled_blocks = list(all_blocks.keys())
print(unfilled_blocks)
# initialize variable pointing to list containing the names of all the unfilled blocks.
# later in the program iterate over this list to verify an input is valid


row1 = (all_blocks.get('a1'),all_blocks.get('a2'),all_blocks.get('a3'),all_blocks.get('a4')); row2 = (all_blocks.get('b1'),all_blocks.get('b2'),all_blocks.get('b3'),all_blocks.get('b4')); row3 = (all_blocks.get('c1'),all_blocks.get('c2'),all_blocks.get('c3'),all_blocks.get('c4')); row4 = (all_blocks.get('d1'),all_blocks.get('d2'),all_blocks.get('d3'),all_blocks.get('d4')); column1 = (all_blocks.get('a1'),all_blocks.get('b1'),all_blocks.get('c1'),all_blocks.get('d1')); column2 = (all_blocks.get('a2'),all_blocks.get('b2'),all_blocks.get('c2'),all_blocks.get('d2')); column3 = (all_blocks.get('a3'),all_blocks.get('b3'),all_blocks.get('c3'),all_blocks.get('d3')); column4 = (all_blocks.get('a4'),all_blocks.get('b4'),all_blocks.get('c4'),all_blocks.get('d4')); square1 = (all_blocks.get('a1'),all_blocks.get('a2'),all_blocks.get('b1'),all_blocks.get('b2')); square2 = (all_blocks.get('a3'),all_blocks.get('a4'),all_blocks.get('b3'),all_blocks.get('b4')); square3 = (all_blocks.get('c1'),all_blocks.get('c2'),all_blocks.get('d1'),all_blocks.get('d2')); square4 = (all_blocks.get('c3'),all_blocks.get('c4'),all_blocks.get('d3'),all_blocks.get('d4'))
# initialize row sub n, column sub n, square sub n variables.
# these variables point to lists containing all the blocks present in a certain row/column/square

corresponding_groupings = {'a1': [row1, column1, square1], 'a2': [row1, column2, square1],'a3': [row1, column3, square2],'a4': [row1, column4, square2],'b1': [row2, column1, square1],'b2': [row2, column2, square1],'b3': [row2, column3, square2],'b4': [row2, column4, square2],'c1': [row3, column1, square3],'c2': [row3, column2, square3],'c3': [row3, column3, square4],'c4': [row3, column4, square4],'d1': [row4, column1, square3],'d2': [row4, column2, square3],'d3': [row4, column3, square4],'d4': [row4, column4, square4]}
# initialize dictionary 

def print_board():
    '''
    This function updates the pointer puzzle_board variable then prints the board for the user
    '''
    puzzle_board = f'''
{(all_blocks.get('a1'))}|{(all_blocks.get('a2'))}|{(all_blocks.get('a3'))}|{(all_blocks.get('a4'))}
-|-|-|-      
{(all_blocks.get('b1'))}|{(all_blocks.get('b2'))}|{(all_blocks.get('b3'))}|{(all_blocks.get('b4'))}
-|-|-|-      
{(all_blocks.get('c1'))}|{(all_blocks.get('c2'))}|{(all_blocks.get('c3'))}|{(all_blocks.get('c4'))}
-|-|-|-      
{(all_blocks.get('d1'))}|{(all_blocks.get('d2'))}|{(all_blocks.get('d3'))}|{(all_blocks.get('d4'))}
'''
    print(f'{puzzle_board}')

def unfilled(any_list):
    '''
    This functions takes 1 argument (a list), clears the list, then populates it with the names of tiles 
    (a1, b3, etc.) that are blank.
    '''
    any_list.clear()
    for key in all_blocks.keys():
        if all_blocks.get(key) == ' ':
            any_list.append(key)
    return(any_list)

def check_valid_input(requested_block, requested_value):
    '''
    This function verifies that a requested input by the user is valid by checking to see if it is
    the value is present already in the corresponding row, column, or cell of the block where the
    inputted value is being requested
    '''
    row1 = (all_blocks.get('a1'),all_blocks.get('a2'),all_blocks.get('a3'),all_blocks.get('a4')); row2 = (all_blocks.get('b1'),all_blocks.get('b2'),all_blocks.get('b3'),all_blocks.get('b4')); row3 = (all_blocks.get('c1'),all_blocks.get('c2'),all_blocks.get('c3'),all_blocks.get('c4')); row4 = (all_blocks.get('d1'),all_blocks.get('d2'),all_blocks.get('d3'),all_blocks.get('d4')); column1 = (all_blocks.get('a1'),all_blocks.get('b1'),all_blocks.get('c1'),all_blocks.get('d1')); column2 = (all_blocks.get('a2'),all_blocks.get('b2'),all_blocks.get('c2'),all_blocks.get('d2')); column3 = (all_blocks.get('a3'),all_blocks.get('b3'),all_blocks.get('c3'),all_blocks.get('d3')); column4 = (all_blocks.get('a4'),all_blocks.get('b4'),all_blocks.get('c4'),all_blocks.get('d4')); square1 = (all_blocks.get('a1'),all_blocks.get('a2'),all_blocks.get('b1'),all_blocks.get('b2')); square2 = (all_blocks.get('a3'),all_blocks.get('a4'),all_blocks.get('b3'),all_blocks.get('b4')); square3 = (all_blocks.get('c1'),all_blocks.get('c2'),all_blocks.get('d1'),all_blocks.get('d2')); square4 = (all_blocks.get('c3'),all_blocks.get('c4'),all_blocks.get('d3'),all_blocks.get('d4'))
    corresponding_groupings = {'a1': [row1, column1, square1], 'a2': [row1, column2, square1],'a3': [row1, column3, square2],'a4': [row1, column4, square2],'b1': [row2, column1, square1],'b2': [row2, column2, square1],'b3': [row2, column3, square2],'b4': [row2, column4, square2],'c1': [row3, column1, square3],'c2': [row3, column2, square3],'c3': [row3, column3, square4],'c4': [row3, column4, square4],'d1': [row4, column1, square3],'d2': [row4, column2, square3],'d3': [row4, column3, square4],'d4': [row4, column4, square4]}
    for grouping in corresponding_groupings.get(requested_block):
        for cell in grouping:
            if cell == requested_value:
                return False
    return True

def quick_win_game():
    '''
    Quickly attempts to solve the Sudoku puzzle. It iterates over each unfilled block and tries 
    all valid inputs (1-4) for each block. If a valid input is found, it updates the 
    'all_blocks' dictionary with that input. If all blocks are filled after these attempts, 
    it prints the solution. Otherwise, it prompts the user to input more values. If the 
    user declines, it resets 'all_blocks' to the state saved in 'temp_board'. Simplest algorithm
    solve a puzzle, but it only works sometimes.
    '''
    global all_blocks
    global temp_board
    valid_inputs = ('1', '2', '3', '4')
    local_unfilled_blocks = unfilled(unfilled_blocks)
    for unfilled_block in local_unfilled_blocks:
        for valid_input in valid_inputs:
            if check_valid_input(unfilled_block, valid_input) is True:   
                all_blocks[unfilled_block] = valid_input
    if len(unfilled(unfilled_blocks)) == 0:
        print('This puzzle was quickly solved.')
        print('This is the solution: ', end='\n')
        print_board()
    else:
        all_blocks = temp_board
        # reverts Sudoku puzzle back to its state before win_game was executed
        brute_win_game()

def brute_win_game():
    '''
    Uses a very similar algorithm to quick_win_game to solve the sudoku puzzle but it tried 50
    attempts. Each attempt the computer takes a different approach since the order of the
    list containing unfilled blocks the computer iterates over is shuffled as is the list
    of valid inputs.
    '''
    global all_blocks
    global temp_board
    runs = 0
    valid_inputs = ['1','2','3','4']
    local_unfilled_blocks = (unfilled(unfilled_blocks))
    while runs < 50:
        shuffled_valid_inputs = list(valid_inputs)
        shuffle(shuffled_valid_inputs)
        shuffled_local_unfilled_blocks = list(local_unfilled_blocks)
        shuffle(shuffled_local_unfilled_blocks)
        for unfilled_block in shuffled_local_unfilled_blocks:
            for valid_input in shuffled_valid_inputs:
                if check_valid_input(unfilled_block, valid_input):
                    all_blocks[unfilled_block] = valid_input
        if len(unfilled(unfilled_blocks)) == 0:
            print('This is the solution: ', end='\n')
            print_board()
            solved = True
            break
        else:
            all_blocks = temp_board
            runs += 1
    if not solved:
        print("This puzzle could not be solved, more values are needed.")
        all_blocks = temp_board
        # reverts Sudoku puzzle back to its state before win_game() was executed
        input_number()

def input_number():
    """
    Allows the user to input values into the Sudoku puzzle. It prompts the user to select 
    a block and input a value (1-4) for that block. It then checks if the input value is 
    valid and updates the 'all_blocks' dictionary if it is. The user can continue to input 
    values until either the puzzle can be solved or they choose to stop. If the puzzle can 
    be solved, it calls the 'win_game()' function. It also handles invalid inputs.
    """
    global temp_board
    add_more_blocks = True; valid_inputs = ('1', '2', '3', '4')
    print('This is the board currently: ', end='\n')
    print_board() 
    print(f"""
Currently, these square have no values: 
{unfilled(unfilled_blocks)}
        """)   
    while len(unfilled(unfilled_blocks)) > 12 or add_more_blocks:
        selected_block = input("Which block would you like to fill: ")
        if selected_block in unfilled(unfilled_blocks):
            selected_valid_input = False
            while not selected_valid_input:
                new_value = input("What value (1-4) shall this new block assume? ")
                if new_value in valid_inputs and check_valid_input(selected_block, new_value) is True:
                    all_blocks[selected_block] = new_value
                    print('This is the board currently: ', end='\n')
                    print_board()
                    if len(unfilled(unfilled_blocks)) < 12:
                        print('The sudoku puzzle can now be attempted to be solved.')
                        add_more_blocks_inp = input('Would you like to input additional values for blocks? (Y)es/(N)o: ')
                        if add_more_blocks_inp.lower() in ('y', 'yes'):
                            add_more_blocks = True
                        else:
                            add_more_blocks = False
                            temp_board = dict(all_blocks)
                            # creates a variable storing the state of the board before win_game was attempted
                            # this is done in case win_game fails then the board can be reverted back to
                            # its original state
                            brute_win_game()
                    selected_valid_input = True
                elif new_value not in valid_inputs:
                    print('That is an invalid input. Valid inputs are "1", "2", "3", and "4"')
                    print('Please try again')
                    continue
                elif check_valid_input(selected_block, new_value) is False:
                    print('''
That is an invalid input. Your requested inputted value
is already either present in the corresponding row/column/square
of the chosen block. Please try again''')
                    continue
        elif selected_block not in unfilled(unfilled_blocks):
            print("That is not the valid name of an unfilled square.")
            print(f"""
Currently, these square have no values: 
{unfilled(unfilled_blocks)}
        """)
            print('Please try again.')
            continue 

print('Please input values.')

if __name__ == "__main__":
    instructions()
    input_number()
