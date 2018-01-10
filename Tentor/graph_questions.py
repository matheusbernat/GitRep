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

def has_loop_v_Malcolm(start_node, graph):
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

def has_loop_v_facit(start, graph):
    """
    Checks if it is possible to reach a loop from start in graph. The graph is
    represented as a dictionary of nodes mapped to a tuple of its children.   
    """
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

svensson = ['Erik', ['Olle', ['Eva', 'Karin', 'Anna'],
                             ['Lars', 'Maria'],
                             ['Pär', 'Sofia']],
                    'Lisa',
                    ['Stina', ['Gunnar', 'Lasse'],
                              'Lennart']]



