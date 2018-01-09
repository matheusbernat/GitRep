################################################
# TENTA 2015, 1
################################################

# FACIT PÅ UPPGIFTERNA JAG INTE LÖSTE:

# Uppgift 4 (komma på vettiga namn, return lista med alla möjliga namn

def combos_facit(word):
    n = len(word)
    res = []
    for left in range(1, n-2+1):
        for right in range(1, n-left-1+1):
            res.append(word[:left]+word[-right:])
    return res

# Uppgift 5 (GRAFUPPGIFTEN! Return vilka noder man skulle komma fram till)

def locations_facit(g, start, steps):
    if start not in g:
        return []
    elif steps <= 0:
        return [start]
    else:
        res = []
        for d in g[start]:
            new = locations(g, d, steps-1)
            for e in new:
                if e not in res:
                    res.append(e)
        return res


################################################################

# Genomgångsläsning i början, 5 min

# UPPGIFT 1, 20 min

def count_similar(str_1, str_2):
    """ Counts how many letters are simliar in two equal-sized strings """
    similar = 0
    for i in range(len(str_1)):
        if str_1[i] == str_2[i]:
            similar += 1
    return similar


def check_alike(str_1, str_2):
    """ Checks whether the first string is alike the second one """
    def help_fn(str_1, str_2):
        if not str_1 or not str_2:
            return 0
        elif str_1[0] == str_2[0]:
            return help_fn(str_1[1:], str_2[1:])
        elif str_1[0] != str_2[0]:
            return 1 + help_fn(str_1, str_2[1:])
    not_alike = help_fn(str_1, str_2)
    return not_alike < 2
    
def close_enough(str_1, str_2):
    if len(str_1) == len(str_2):
        return len(str_1) - count_similar(str_1, str_2) <= 1
    elif len(str_1) < len(str_2):
        return check_alike(str_1, str_2)
    else:
        return check_alike(str_2, str_1)


# UPPGIFT 2, 20 min

def uniq_r(seq):
    if not seq:
        return []
    elif len(seq) == 1 or seq[0] != seq[1]:
        return [seq[0]] + uniq_r(seq[1:])
    elif seq[0] == seq[1]:
        return uniq_r(seq[1:])

def uniq_i(seq):
    final_seq = [seq[0]]
    for i in range(len(seq) - 1):
        if seq[i] != final_seq[-1]:
            final_seq.append(seq[i])
    return final_seq

# UPPGIFT 3, 30 min

def gen_find(seq, func, underlist):
    """ Checks whether an element in a given list fulfills the functions req """
    if not seq:
        return False
    if underlist == True:
        if isinstance(seq[0], list):
            return gen_find(seq[0], func, underlist) or \
                   gen_find(seq[1:], func, underlist) 
    if func(seq[0]):
        return True
    else:
        return gen_find(seq[1:], func, underlist)

def where(seq, elem):
    """ Locates position of an element in a given list """
    if not gen_find(seq, (lambda x: x == elem), True):
        return "no"
    elif gen_find(seq, (lambda x: x == elem), False):
        return "top"
    else:
        return "deep"

# UPPGIFT 4, 40 min
"""
def combos(string):
    #Generates all possible combinations of words by taking letters from mid
"""
    
# UPPGIFT 5, 50 min

g = {'a':('d'), 'b':('a'), 'c':('b', 'd', 'f'), 'd':('h'), 'e':(),
 'f':('e', 'g'), 'g':('h'), 'h':('f', 'i'), 'i':('j'), 'j':('h')}

def locations(graph, start, steps):
    """ Returns a list of nodes that can be reached leading out from our given """
    if start not in graph:
        return []
    elif steps <= 0:
        return [start]
    else:
        res = []
        for kids in graph[start]:
            new = locations(graph, kids, steps-1)
            for a in new:
                if a not in res:
                    res.append(a)
        return res

# UPPGIFT 6, 60 min

# Löste uppgift A

# TOTALT: 220 min, 80 min kvar för genomgång
