"SEMINARIE 7"
"""PROBLEMLÖSNING:
1) förstå!
  - indata, utdata
  - begrepp, ord
  - få en tydlig bild av det som måste göras
2) ta fram en plan
  - analysera
  - dela upp i mindre delar
  - lös enklare variant
3) implementera, skriva kod
4) utvärdera, testa

liggande stolen, ja
brödrecept ja
newtons lagar nej 
list-typen i python, nej datastruktur
not and port ja (se det som if sats)
pythagoras nej (av samma anledning som f=mv)
"""

def bubblesort(seq):
    n = len(seq)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n-1):
            if seq[i-1] > seq[i]:
                big_element = seq[i-1]
                small_element = seq[i]
                seq[i] = big_element
                seq[i-1] = small_element
                swapped = True
    return seq

"""
Top-down och bottom-up
Top-down:
- börja från top och gå ner
- fördelar: strukturerat, man ser den stora bilden
- nackdelar: svårt å testa, tar länge förrän man vet om det funkar

Bottom-up: 
- börja från de små komponenterna och försöka kombinera med alla andra
- fördelar: enkelt å testa
- nackdelar: svårt å se vad man ska göra så att man inte skapar saker i onödan

Bizú: blandning av top-down och bottom-up. 

Algoritmkomplexitet:
- olika sorters: tidskomplexitet, minneskomplexitet (hur mkt tid det tar, etc)
- vad betyder att en algoritm är mer komplex än andra? 
- handlar om hur problemet skalas när indatan ökas
"""

