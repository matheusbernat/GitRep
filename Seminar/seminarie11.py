"SEMINARIE 11"
"""
Hjälpmedel: textbok, anteckningar, pennor, tomma papper, python.org(dokumentationsdelen)
Kriterier: samma namn på funktioner, självbeskrivande namn, strukturererad, följa kraven, kolla upp körexemplen i uppgiften, generell lösning.
"""
# EXEMPELTENTA
from random import randint

# Uppgift 1

def id(name, sirname):
    return name[:3].lower() + sirname[:2].lower() + str(randint(100, 999))

# Uppgift 2

def replace_i(old_elem, new_elem, lst):
    new_lst = []
    for elem in lst:
        if elem == old_elem:
            new_lst.append(new_elem)
        else:
            new_lst.append(elem)
    return new_lst


def replace_r(old_elem, new_elem, lst):
    if not lst:
        return []
    if lst[0] == old_elem:
        return [new_elem] + replace_r(old_elem, new_elem, lst[1:])
    else:
        return [lst[0]] + replace_r(old_elem, new_elem, lst[1:])

# Uppgift 3
    
def collector(func, lst):
    if not lst:
        return []
    elif isinstance(lst[0], list):
        return collector(func, lst[0]) + collector(func, lst[1:])
    elif func(lst[0]):
        return [lst[0]] + collector(func, lst[1:])
    else:
        return collector(func, lst[1:])

    
def numbers_in_interval(lower_bound, upper_bound, lst):
    return collector((lambda x: isinstance(x, int) and \
                      lower_bound<= x <= upper_bound), lst)

# Uppgift 4
"""
def make_move(board, piece, position):
    if is_free(position, board):
        new_row = change_piece(piece, position_column(position), board[position[0]])
        new_board = change_row(new_row, position_row(position), board)
        return new_board
    return False

def is_winner(board, piece):
    for comb in WINNING_COMBINATIONS:
        if check_combination(board, piece, posseq):
            return True
    return False

def check_combinations(board, piece, posseq):
    if is_empty_posseq(posseq):
        return True
    else:
        pos = first_position(posseq)
        c, r = position_column(pos), position_row(pos)
        return is_same_piece(piece, row_piece(c, board_row(r, board))) \
            and check_combination(board, piece, rest_posseq(posseq))
"""
# Uppgift 5

test_graph = {'a': ('b', 'd'), 'b': ('c'), 'c': ('d'), 'd': ('b', 'e'), 
                'e': ('f'), 'f': ()}

def has_loop(start_node, graph):
    def loop_check(node, visited):
        if node in visited:
            return True
        else:
            return check_children(graph[node], [node] + visited)
    def check_children(nodes, visited): # behöver inte ta graph som parameter
        if not nodes:
            return False
        else:
            res = loop_check(nodes[0], visited)
            if res:
                return True
            else:
                return check_children(nodes[0], visited) or \
                check_children(nodes[1:], visited)
    return loop_check(start_node, [])
    






    











        

