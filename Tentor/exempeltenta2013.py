"EXEMPELTENTA 2013"

"Uppgift 1"
from random import randint

def id(name, surname):
    """
    Creates a LiU-id for a person given the person's first and last name
    and put it together with a random number between 100 and 999.
    returns: LiU-id (str)
    """
    return name[:3].lower() + surname[:2].lower() + str(randint(100,999))


"Uppgift 2"

def replace_r(old_element, new_element, lst):
    """
    Recursiv function that changes old_element to new_element, in the case
    that old_element exist in the list lst.
    returns: a new list just like lst but with old_element exchanged for new_element
    """
    if not lst:
        return []
    if lst[0] == old_element: # skulle det vara if eller elif??????
        return [new_element] + replace_r(old_element, new_element, lst[1:])
    else:
        return [lst[0]] + replace_r(old_element, new_element, lst[1:])


def replace_i(old_element, new_element, lst):
    """
    Iterative function that changes old_element to new_element, in the case
    that old_element exist in the list lst.
    returns: a new list just like lst but with old_element exhanged for new_element
    """
    new_lst = []
    for element in lst:
        if element == old_element:
            new_lst.append(new_element)
        else:
            new_lst.append(element)
    return new_lst


"Uppgift 3"
"Deluppgift 3A"

def collector(func, lst):  #FRÅGA: vad är en "högre ordnings funktion"?
    """
    Recursive function that goes through all the elements in the list lst.
    If the element fills the requirement that function func imposes, the 
    element is then added to a new list which is returned in the end.
    returns: a new list (list)
    """
    if not lst:
        return []
    if isinstance(lst[0], list):
        return collector(func, lst[0]) + collector(func, lst[1:])
    if func(lst[0]):
        return [lst[0]] + collector(func, lst[1:])
    else:
        return collector(func, lst[1:])

"Deluppgift 3B"

def numbers_in_interval(begin, end, lst):
    """
    Returns a new list number_lst that consists of all numbers in lst that
    are between the numbers begin and end, with the help of function collector.
    returns: number_lst (list)
    """
    """FRÅGA: do we need to explain how the function works in detail  in Docstrings? 
     Or is it enough to say in general terms as I did?"""

    number_lst = collector((lambda x: isinstance(x, int)), lst)
    for number in number_lst:
        if number < begin or number > end:
            number_lst.remove(number)
    return number_lst


"Uppgift 4"
"Deluppgift 4A"

def make_move():
    """
    Updates the board after the player made a new move.
    """
    "n sei por enquanto"
    pass
"Deluppgift 4B"

def is_winner():
    pass

"Uppgift 5" "n deu"

test_graph = {'a': ('b', 'd'), 'b': ('c'), 'c': ('d'), 'd': ('b', 'e'), 
                'e': ('f'), 'f': ()}

def has_loop(beginning_element, graph):
    """
    Function that controls whether we fall into an infinite loop from a starting
    point beginning_element.
    returns: True or False (boole)
    """
    def boole_value(visited):
        if node in visited:
            return True
        if not node:
            return False
    def check_node():
        pass
    if not graph[beginning_element]: #dvs om den är lika med ()
        return False
    if beginning_element == graph[beginning_element]:
        return True
    if graph[beginning_element]:
        return has_loop(graph[beginning_element][0], graph) or \
               has_loop(graph[beginning_element][1], graph) 

"Uppgift 6"

def give_change(change):
    """
    Function that calculates the change that shall be given back. It takes as
    an input the change amount, and returns a list of the cash that shall be 
    given back.
    returns: list 
    """
    if not change:  #dvs om change = 0
        return []
    if change // 100 >= 1:
        return (change//100)*[100] + give_change(change-(change//100)*100)
    elif change // 50 == 1:
        return [50] + give_change(change-50)
    elif change // 20 >= 1:
        return (change//20)*[20] + give_change(change-(change//20)*20)
    elif change // 5 >= 1:
        return (change//5)*[5] + give_change(change-(change//5)*5)
    elif change // 1 >= 1:
        return (change//1)*[1] + give_change(change-(change//1)*1)


def give_change3(change):   "facit" "mkt bättre för här finns det ingen kodupprepning som det gör i min funktion"
    res = []
    for value in [500, 100, 50, 20, 5, 1]:
        while change >= value:
            res.append(value)
            change -= value
    return res
