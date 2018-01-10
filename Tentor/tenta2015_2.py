# TENTA 2015, 2

from grammatik_s import *

################ FRÅGOR JAG INTE KUNDE LÖSA, FACIT ###################

# Uppgift 1b
def column_facit(s, size):
    res = []
    separators = " .,:;!?"
    i = size - 1
    while True:
        if len(s) <= 1:
            res.append(s)
            break
        elif i <= 0:
            res.append(s[0:1])
            s = s[1:]
            i = size - 1
        elif s[i] in separators:
            res.append(s[0:i+1])
            s = s[i+1:]
            i = size - 1
        else:
            i -= 1
    return res

# Uppgift 5
def distance_facit(tree, start, end):
    def walk(node, dist):
        if node == goal:
            return dist
        else:
            children = tree[node]
            if not children:
                return -1
            else:
                for tup in children:
                    res = walk(get_node(tup), d + get_dist(tup))
                    if res > 0:
                        return res
                    return -1
    return walk(start, 0)



#####################################################################

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
            return 0
        elif seq[0] == elem:
            return 0
        else:
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

# OR:

def find_i_facit(seq, elem):
    for i in range(len(seq)):
        if seq[i] == elem):
            return i
    return -1
    
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

# OR

def make_interval_facit(seq, begin, end, elem):
    return mark_interval(seq,(lambda x:isinstance(x,int) and (begin<=x<=end), e))

# UPPGIFT 4

def contain_r(small, big):
    """ Checks whether a given small message exists within the big one. Recurs """
    if not big and small:
        return False
    elif not small:
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
    return message == small:

# OR:

def contain_i_facit(small, big):
    for e in large:
        if small and e == smal[0]:
            small = small[1:]
    return not small

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
            new = distance(tree, get_node(tup), end)
            for e in tree[get_node(tup)]:
                travelled += get_dist(e)
        return travelled

# UPPGIFT 6

def find_rules(cat, g): 
    "category x grammar -> grammar"
    return extract_grammar(grammar, (lambda x: x == cat))
    
def extract_grammar(g, fn):
    "category x grammar -> grammar"
    if is_empty_grammar(g):
        return create_grammar()
    elif fn(first_rule(g)):
        return [first_rule(g)] + find_rules(cat, rest_grammar(g))
    else:
        return find_rules(cat, rest_grammar(g))

def generate_sentence(cat, lex, gram):
    "category x lexicon x grammar -> sentence"
    
       
        
    
    
