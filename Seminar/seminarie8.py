"SEMINARIE 8"
# interpreterat språk (interpretator tex Python, Java Script): översätter sad för rad (tolk)
# + debuggning kan vara enklare att implementera
# + ingen kompilering behövs
# + om mnan har källkoden funkar det var som helst (mac, windows, ...)
# - långsam (speciellt för stora program)
# - källkod bevaras ej hemligt, det syns

# kompilerat språk (kompilator tex C++): översätter hela språket, maskinkod
# + snabba
# + ofta kan köras direkt utan å ladda ner stuff
# + fel upptäcks även innan man kör programmet
# - tar tid att kompilera

# S = a, aaa, aab, ba, bb

def check_1(string):
    lan1 = ['a', 'aaa', 'aab','ba', 'bb']
    if string in lan1:
        return True
    else: 
        return False

def check_letters(string):
    for letter in string:
        if letter not in 'ab':
            return False
    return True

def check_2(string):
    if string == string[::-1] and check_letters(string):
        return True
    else:
        return False

def oldest_branch(graph, person):
    sum = 0
    for child in graph[person][0]:
        oldest_branch(graph, child[0][0])
        sum += child[1]
    return sum

dictio = {'Ada': (['Alan', 'Herbert'], 36),
          'Alan': ([], 41),
          'Herbert': (['Charles'], 84)}


def get_children(g, person):
    return g[person][0]
    
def get_age(g, person):
    return g[person][1]

def oldest_branch(g, p):
    oldest = 0
    for child in get_children(g, p):
        age = oldest_branch(g, child)
        if age > oldest:
            oldest = age
    return oldest + get_age(g, p)

    
