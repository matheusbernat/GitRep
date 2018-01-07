################################################
# TENTA 2015, 1
################################################

# Genomgångsläsning i början, 5 min

# UPPGIFT 1, 20 min

def count_similar(str_1, str_2):
    """ Counts how many letters are simliar in two equal-sized strings """
    similar = 0
    for i in range(len(str_1)):
        if str_1[i] == str_2[i]:
            similar += 1
    return similar
"""
def check_alike(str_1, str_2):
    #Checks whether the first string is alike the second one
    if not str_1 or not str_2:
        return False
    if str_1[0] == str_2[0]:
        return check_alike(str_1[1:], str_2[1:])
    elif str_1[0] != str_2[0]:
        return check_alike(str_1, str_2[1:])
    else:
        return True
"""

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
    if not seq:
        return False
    elif func(seq[0]):
        return True
    elif underlist == True:
        if isinstance(seq[0], list):
            return gen_find(seq[0], func, underlist) or \
                   gen_find(seq[1:], func, underlist) 
    else:
        return gen_find(seq[1:], func, underlist)

# UPPGIFT 4, 40 min


# UPPGIFT 5, 50 min


# UPPGIFT 6, 60 min


# TOTALT: 220 min, 80 min kvar för genomgång
