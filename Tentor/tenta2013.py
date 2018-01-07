"TENTA 2013"

"Uppgift 1" #bilda skykrapor med hashtags. 

from random import randint 
"FRÅGA: är det bäst att importera funktionen här? eller i början på allt?" "RESPOSTA: importa aqui"

def manhattan(width, min_heigth, max_heigth): #N FIZ
    """
    Creates a random figure with hashtags # that shall represent a skyscraper.
    It takes as input three integers.
    """
    heigth = randint(min_heigth, max_heigth)
    space = 0
    width_temp = width -1
    while heigth:
        print(space * " ", (width - width_temp) * "#")
        width_temp -= 1
        heigth -= 1
        space += 1


"Uppgift 2" #skapa insert funktionen rekursivt och iterativt 

def inser_r(pos, element, lst): #N FIZ
    if pos == 0:
        return [pos] + lst
    else:
        return [lst[0]] + inser_r(pos-1, element, lst)

"APRENDIZADO: inte alla rekursiva funktioner behöver ha if not... return [] i början!"
"det där pos-1 var ett riktigt smart sätt å lösa det på, för pos blir en mindre varje gång vi kör lst[1:]"


def inser_i(ind, element,lst): #OK
    new_lst = []
    for i in range(len(lst)):
        if ind == i:
            new_lst.append(element)
            new_lst.append(lst[i])
        else:
            new_lst.append(lst[i])
    return new_lst


"Uppgift 3" "OK"

def remover(func, lst): #OK
    if not lst:
        return []
    if isinstance(lst[0], list):
        return [remover(func, lst[0])] + remover(func, lst[1:])
    if not func(lst[0]):
        return [lst[0]] + remover(func, lst[1:])
    else:
        return remover(func, lst[1:])


def rem_values(min_value, max_value, lst): #OK
    return remover(lambda x: x in range(min_value, max_value + 1), lst)


"Uppgift 4"

def count_level(lvl, seq): #N FIZ
    """
    Counts the quantity of elements in a list that are in the given level.
    """
    if not seq or lvl == 0:
        return 0
    elif isinstance(seq[0], list):
        return count_level(lvl - 1, seq[0]) + count_level(lvl, seq[1:])
    elif lvl == 1:
        return 1 + count_level(lvl, seq[1:])
    else:
        return count_level(lvl, seq[1:])

"Uppgift 5" "N FIZ"

"""
def ancestors(person, family_tree):
   if not family_tree:
        return []
    if isinstance(family_tree[0], list):
        return ancestors(person, family_tree[0]) +ancestors(person, family_tree[1:])
    
    """

svensson = ['Erik', ['Olle', ['Eva', 'Karin', 'Anna'],
                             ['Lars', 'Maria'],
                             ['Pär', 'Sofia']],
                    'Lisa',
                    ['Stina', ['Gunnar', 'Lasse'],
                              'Lennart']]

def ancestors(person, tree):
    if isinstance(tree, str):
        if person == tree:
            return [person]
        else:
            return []
    elif person == tree[0]:
        return [person]
    else:
        for child_tree in tree[1:]:
            result = ancestors(person, child_tree)
            if result:
                return [tree[0]] + result
        return []




"Uppgift 1, andra försök"

def manhattan(width, low, high):
    floor_seq = []
    for floor in range(randint(low, high)-1):
        floor_seq.append(randint(0,width)*"#")
    floor_seq.append(width*"#") #vi försäkrar oss att bottenvåningen har width st #
    
"Uppgift 4, andra försök" "saiu"

def count_level(lvl, seq):
    if lvl == 0 or not seq:
        return 0 
    if (isinstance(seq[0], int) or isinstance(seq[0], float) or isinstance(seq[0], str)) and lvl == 1:
        return 1 + count_level(lvl, seq[1:])
    if isinstance(seq[0], list):
        return count_level(lvl-1, seq[0]) + count_level(lvl, seq[1:])
    else:
        return count_level(lvl, seq[1:])
    
        
    
