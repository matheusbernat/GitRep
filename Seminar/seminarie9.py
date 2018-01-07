"SEMINARIE 9"
#lärde mig set(): a list without ordning. med brackets ist för hakparenteser

# räkna Euler väg

dictio = {"A":["B", "C"],
          "B":["A", "C"],
          "C":["A", "B", "D", "G"],
          "G":["C", "H"],
          "H":["G"],
          "D":["C", "E", "F"],
          "E":["D", "F"],
          "F":["E", "D"]}

def check_euler(table):
    uneven_numbers = 0
    for key in table:
        if len(table[key]) % 2 == 1:
            uneven_numbers += 1
    return uneven_numbers == 0 or uneven_numbers == 2




# SUDOKU

sudoku_board = [
        [2, 9, 5, 7, 4, 3, 8, 6, 1],
        [4, 3, 1, 8, 6, 5, 9, 2, 7],
        [8, 7, 6, 1, 9, 2, 5, 4, 3],
        [3, 8, 7, 4, 5, 9, 2, 1, 6],
        [6, 1, 2, 3, 8, 7, 4, 9, 5],
        [5, 4, 9, 2, 1, 6, 7, 3, 8],
        [7, 6, 3, 5, 2, 4, 1, 8, 9],
        [9, 2, 8, 6, 7, 1, 3, 5, 4],
        [1, 5, 4, 9, 3, 8, 6, 7, 2]
    ]

def is_valid(seen):
    """ Checks if the elements in seen is the numbers 1 through 9 """
    valid = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return seen == valid

def check_row(board, row):
    """ Checks if a row is a correct sudoku row (it contains numbers 1 through 9) """
    seen = set() # a list without ordning, not a dictionary
    for col in range(9): # so that we check all 10 columns
        seen.add(board[row][col])
    return is_valid(seen)
"""
def check_board(board):
    if len(board) != 9: #checks size of the board
        return False
    for row in board:   # checks size of the rows
        if len(row) != 9:
            return False
"""

"Malcolms lösning"

def check_row(board, row):
    """ Checks if a row is a correct sudoku row (it contains numbers 1 through 9) """
    seen = set() # a list without ordning, not a dictionary
    for col in range(9): # so that we check all 10 columns
        seen.add(board[row][col])
    return is_valid(seen)

def check_col(board, col):
    """ Checks if a column is a correct sudoku column (it contains numbers 1 through 9) """
    seen = set() # a list without ordning, not a dictionary
    for row in range(9): # so that we check all 10 columns
        seen.add(board[row][col])
    return is_valid(seen)

def check_block(board, i):
    x = i % 3 # i mod 3
    y = i // 3

    seen = set()
    for row in range(x*3, 3 + x*3):
        for col in range(y*3, 3 + y*3):
            seen.add(board[row][col])
    return is_valid(seen)
            

def check_board(board): ###########IMPORTANTE lär dig det med return false o tr
    for i in range(9):
        ok = check_row(board, row) and check_col(board, col)\
             and check_block(board, i)
        if not ok:
            return False
    return True

        
check_board()

    
    
        
        
