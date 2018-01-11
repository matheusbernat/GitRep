######################################################
# Uppgifter med GRAFER
######################################################

# Uppgift 1 (lista ut äldsta grenen i ett träd) (seminar 8)

def oldest_branch(g, p):
    oldest = 0
    for child in get_children(g, p):
        age = oldest_branch(g, child)
        if age > oldest:
            oldest = age
    return oldest + get_age(g, p)

def get_children(g, person):
    return g[person][0]
    
def get_age(g, person):
    return g[person][1]

dictio = {'Ada': (['Alan', 'Herbert'], 36),
          'Alan': ([], 41),
          'Herbert': (['Charles'], 84)}

# Uppgift 2 - check whether we can get into an infinite loop (seminar 11)

def has_loop_facit(start, graph):
    def loop_check(node, visited):
        if node in visited:
            return True
        else:
            return check_children(graph[node], [node] + visited)
    def check_children(node_list, visited):
        if not node_list:
            return False
        else:
            res = loop_check(node_list[0], visited)
            if res:
                return res
            else:
                return check_children(node_list[1:], visited)

    return loop_check(start, [])

test_graph = {'a': ('b', 'd'), 'b': ('c'), 'c': ('d'), 'd': ('b', 'e'), 
                'e': ('f'), 'f': ()}

# Uppgift 3 - given a person, determine its ancestors (tenta 2013)

def ancestors(person, tree):
    if isinstance(tree, str): #HUR SKULLE tree ENS BLI EN STRÄNG?
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

svensson = ['Erik', ['Olle', ['Eva', 'Karin', 'Anna'],
                             ['Lars', 'Maria'],
                             ['Pär', 'Sofia']],
                    'Lisa',
                    ['Stina', ['Gunnar', 'Lasse'],
                              'Lennart']]

# Uppgift 4 (GRAFUPPGIFTEN! Return vilka noder man skulle komma fram till)(tenta 2015_2)

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

# Uppgift 5 (uppger distance form en node till en annan. Returnerar -1 om det e omöjligt)(tenta 2015_2)
def get_node(tup):
    return tup[0]

def get_dist(tup):
    return tup[1]

def distance_facit(tree, start, goal):
    def walk(pos, dist):
        if pos == goal:
            return dist
        else:
            children = tree[pos]
            if not children:
                return -1
            else:
                for pair in children:
                    res = walk(pair[0], dist + pair[1])
                    if res > 0:
                        return res
                    return -1
    return walk(start, 0)

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
