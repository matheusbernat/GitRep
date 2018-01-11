####################################
# SVÅRARE UPPGIFTER - 5 o 6
####################################

# Grafuppgifter

# Tenta





# Tenta 2015_2

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

def distance(tree, start, end): # funkar inte alls bra, bara för a-b och a-e
    def walk(dist, start, end):
        print("1. dist =", dist)
        if start == end:
            print("THE END.", "start = end =", start)
            return 0
        else:
            print("start =", start)
            for tup in tree[start]:
                print("3.", "tree[start] =", tree[start])
                print("4.", "tup =", tup)
                dist += get_dist(tup)
                print("5. dist =", dist)
                print("gonna calculate new_dist")
                new_dist = walk(0, get_node(tup), end)
                print("new_dist =", new_dist)
                if new_dist:
                    dist += new_dist
                    print("6. dist =", dist)
                if dist:
                    return dist
                return -1
    return walk(0, start, end)

def distance_2(tree, start, end):
    def walk(node, dist):
        print("1. dist =", dist)
        if node == end:
            print("THE END.", "start = end =", start)
            return dist
        else:
            for tup in tree[node]:
                print("2.", "tree[node] =", tree[node])
                res = walk(get_node(tup), get_dist(tup) + dist)
                print("3.", "res =", res)
                return res
    return walk(start, 0)

def distance_3(tree, start, end):
    def walk(node, dist):
        if node == end:
            return dist
        else:
            children = tree[node]
            if not children:
                return -1
            else:
                for pair in children:
                    res = walk(pair[0], dist + pair[1])
                    if res > 0:
                        return res
                    return -1
    return walk(start, 0)
                
    




















# Tenta 2014_1
children = {'Linus': ('Eva', 'Per'),
 'Linnea': ('Per', ),
 'Eva': ('Emilia', 'Emil'),
 'Per': ('Stina', ),
 'Stina': ('Lillan', )} 


def descendants(start, tree): # funkar typ, resultat är ej rak lista
    res = []
    #print("1.", "start", start)
    if start not in tree:
        return []
    else:
        for person in tree[start]:
            #print("2.", "tree[start] =", tree[start])
            #print("3.", "person =", person)
            if person not in res:
                res.append(person)
                #print("4. appending", person)
                #print("provisory res =", res)
            new_person = descendants(person, tree)
            #print("5.", "new_person =", new_person)
            if new_person not in res and new_person:
                res.append(new_person)
                #print("6. appending", new_person)
    return res

def new_descendants(start, tree):
    def get_descendants(res = []):
        if start not in tree:
            return []
        else:
            for person in tree[start]:
                if person not in res:
                    res.append(person)
                new_person = new_descendants(person, tree)
                if new_person not in res and new_person:
                    res.append(new_person)
        return res
    def get_straight(seq):
        if not seq:
            return []
        elif isinstance(seq[0], list):
            return get_straight(seq[0]) + get_straight(seq[1:])
        else:
            return [seq[0]] + get_straight(seq[1:])
    return get_straight(get_descendants())
    

# Tenta 2013 (given a person, find it's ancestor)

svensson = ['Erik', ['Olle', ['Eva', 'Karin', 'Anna'],
                               ['Lars', 'Maria'],
                               ['Pär', 'Sofia']],
                      'Lisa',
                      ['Stina', ['Gunnar', 'Lasse'],
                                'Lennart']]

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
            if result:#i.e. om personen vi letade efter hittades (person == tree)
                return [tree[0]] + result
            else:
                return []

        
# Exempeltenta (has loop)

example_graph = {'a': ('b', 'd'),
              'b': ('c'),
              'c': ('d'),
              'd': ('b', 'e'), 
              'e': ('f'),
              'f': ()}

def has_loop(start, graph):
    def loop_check(node, visited):
        if node in visited:
            return True
        else:
            return check_children(graph[node], [node] + visited)
    def check_children(children, visited):
        if not children: 
            return False
        else:
            res = loop_check(children[0], visited)
            if res: # DÚVIDA: HUR SKULLE 'res' INTE FINNAS? res = True/False
                return res
            else:
                return check_children(children[1:], visited)
            
    return loop_check(start, [])


    



# Testing some graph exercises

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_path(start, end, tree, path = []):
    path = path + [start]
    #print("1)", "path =", path)
    if (start or end) not in tree:
        return []
    elif start == end:
        #print("The End.", "start = end =", start)
        return path
    else:
        for children in tree[start]:
            #print("2)", "children =", children)
            if children not in path:
                new_path = find_path(children, end, tree, path)
                if new_path:
                    #print("3)", "new_path =", new_path)
                    return new_path
        return None

def find_all_paths(start, end, tree, path = []):
    path = path + [start]
    #print("1)", "path =", path)
    if start == end:
        #print("1", "start = end =", start)
        return path
    else:
        path_list = []
        for children in tree[start]:
            #print("2)", "children =", children)
            if children not in path:
                new_path = find_all_paths(children, end, tree, path)
                if new_path:
                    #print("3)", "new_path =", new_path)
                    path_list.append(new_path)
                else:
                    return None
        return path_list

def find_shortest_path(start, end, tree, path = []):
    path = path + [start]
    if start == end:
        return path
    else:
        shortest = []
        for child in tree[start]:
            if child not in path:
                if child not in path:
                    new_path = find_shortest_path(child, end, tree, path)
                    if new_path:
                        if not shortest or len(new_path) < len(shortest):
                            shortest = new_path
        return shortest
    
