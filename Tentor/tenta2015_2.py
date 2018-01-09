# TENTA 2015, 2

# UPPGIFT 1

def split(string, size):
    """ Splits a string in a bunch of strings with a given size """
    res = []
    help_str = string
    while help_str:
        res.append(help_str[:size])
        help_str = help_str[size:]
    return res

"""
def column(string, size):
    sep = " .,:;!?"
    res = []
    new = string
    while new:
        for i in range(size):
            if str(new[size - i]) in sep:
                res.append(new[:size])
                new = new[size:]
"""

# UPPGIFT 2 

def find_r(seq, elem):
    """ Recursive fn returns the index of an element in a list. If no elem: -1 """
    def help_fn(seq, elem):
        if not seq:
            #print("a")
            return 0
        elif seq[0] == elem:
            #print("b")
            return 0
        else:
            #print("c")
            return 1 + help_fn(seq[1:], elem)
    if help_fn(seq, elem) == len(seq):
        return -1
    else:
        return help_fn(seq, elem)

def find_i(seq, elem):
    """ Iterative fn returns the index of an element in a list. If no elem: -1 """
    res = 0
    for el in seq:
        if el == elem:
            break
        else:
            res += 1
    if res == len(seq):
        return -1
    else:
        return res
    
# UPPGIFT 3

def insert_after(seq, func, elem):
    copy = []
    for el in seq:
        if func(el):
            copy.append(el)
            copy.append(elem)
        else:
            copy.append(el)
    return copy

def mark_interval(seq, begin, end, elem):
    res = []
    for el in seq:
        if isinstance(el, str) or el not in list(range(begin, end+1)):
            res.append(el)
        else:
            res.append(el)
            res.append(elem)
    return res

# UPPGIFT 4

def contain_r(small, big):
    """ Checks whether a given small message exists within the big one. Recurs """
    if not big and small:
        return False
    elif (not big and not small) or not small:
        return True
    elif big[0] == small[0]:
        return contain_r(small[1:], big[1:])
    else:
        return contain_r(small, big[1:])

def contain_i(small, big):
    """ Checks whether a given small message exists within the big one. Iterat """
    message = ''
    for letter in small:
        for i in range(len(big)-1):
            if big[i] == letter:
                message += big[i]
                big = big[i:]
                break
    if message == small:
        return True
    else:
        return False

# UPPGIFT 5

t = {'a': (('b', 4), ('c', 7), ('d', 3)),
     'b': (('e', 2), ('f', 9)),
     'c': (('g', 5), ),
     'd': (('h', 4), ('i', 3)),
     'e': (),
     'f': (),
     'g': (('j', 2), ('k', 1), ('l', 8)),
     'h': (),
     'i': (('m', 6), ),
     'j': (),
     'k': (),
     'l': (),
     'm': ()}

def get_node(tup):
    return tup[0]

def get_dist(tup):
    return tup[1]

def distance(tree, start, end):
    if (start not in tree) or (end not in tree): #or no possible way:
        return -1
    elif start == end:
        return 0
    else:
        travelled = 0
        for tup in tree[start]:
            print("tup =",tup)
            new = distance(tree, get_node(tup), end)
            for e in tree[get_node(tup)]:
                travelled += get_dist(e)
        return travelled

# UPPGIFT 6
