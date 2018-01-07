# ATT FÅ HJÄLP
#På tentan: skriv "help(namnet_på_funktionen)".
# str.format användbar. "x: {}, y: {}".format(x = , y= ,) x=,y=
# cv2.threshold : returnerar 1 eller 0, binära färger
# cv2.blur sudda bilden, ej skarpa kanter
# cv2.mean räknar ut medelvärdet på pixels
# 1)Analys (identifiera vad det är vi ska lösa), 
# 2)Specifikation (formaliserar vad programmet ska göra exakt)
# 3)Design (skissa hur programmet ska se ut, vad varje del gör)
# 4)Implementation (översätter saker till kod)
# 5)Testning
# 6)Underhåll (extra grejer)

# x = [i**2 for x in range(10)]


import math
math.cos(math.pi)
# skriv så på stora program där man inte vet var funktioner kommer ifrån

#ELLER:

from math import cos, pi # eller from math import *

#1) [i for i in range(10)] =  [0,1,2,3,4,5,6,7,8,9
#2) [i for i in range(10) if i % 2] = [0,2,4,6,8] FEL [1,3,5,7,9]
#3) [[x for x in range(0,3)] for y in range(0,3)] = [[0,1,2],[0,1,2],[0,1,2]]
#4) [[0, 4, 8]] FEL
#5) ["b,n,n"] 

#1)

#seq = [new_word for word in ["citron","banan","apelsin"] if 'a' in word] FEL
x = [elem.replace('a', '*') for elem in ["banan","apa","citron"] if 'a' in elem]

seq2 = [x for x in range(100) if (x % 3 == 0 or x % 5 == 0) and x % 15 != 0]

seq3 = [[(1 if x == y else 0) for x in range(4)] for y in range(4)]

def test():
    testseq = []
    for y in range(5):
        for x in range(5):
            if x == y:
                testseq.append([1])
            else:
                testseq.append([0])
    return testseq

def t(lst):
    for elem in lst:
        elem = [[elem]]
    return lst
 
