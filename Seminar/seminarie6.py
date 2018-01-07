"""
FEL
När/hur upptäcks fel? vid testning, vid användning
Vad kan orsaka fel? glömma synca programmet, stavfel, fel variabelnamn

Metoder för felsökning: debugprintar, debugger, lösa igenom koden noga, 
visa/förklara koden för nån annan, halvering (binär sökning), ta en paus
"""

"""
UNDANTAG (error)
Förutse att error kommer uppstå: använd try/except"""
def try_get_lines_in_file(filename):
    try:
         f = open(filename)
         lines = f.readlines()
         f.close()
         return lines
    except Python Error......
         return []
"""
TypeError: ['a'] + 4
IndexError: ['a'][1000]
IndentError: indenteringsfel
ValueError: sqr(-1) finns ej
RuntimeError: något oförutsett

Hur man kastar error(undantag): raise ValueError("aoifeub") 
meddelandet skrivs ut när felet uppstår
"""

"""
TESTNING
Enhetstestning: testa minsta beståndsdel av programmet (varje del för sig)
Integrationstestning: testa om 2 eller fler funktioner funkar tillsammans
Systemstestning: testa om hela skiten funkar (om input o output stämmer)
Acceptanstestning: programmet uppfyller kundens specifikationer
White-box-testning: kollar på programmet inifrån, vad den gör exakt
Black-box-testning: kollar på programmet utifrån, på resultat

Fördel white-box: mer sannolikt att man upptäcker fel
Fördel black-box: snabbare
"""

"""
PROGRAMMERINGSPRAXIS
- docstrings med citationstecken ("") ej #
- if ... True: ----- True är onödigt
- självförklarande variablenamn
"""

"""
GIT
git blame 'sort.py' ------- visar vem som ändrade o på vad
git status kollar vad som finns lokalt. 
git commit -m : m står för message. om du inte kör -m öppnas en texteditor
git commit -am : addar allt du ändrade på
git diff: visar vad du ändrat innan commit
BRA Å PULLA varje gång man börjar ändrar på kod
om man ändrat på samma ställe: git ändrar koden o visar de olika sakerna
båda ändrade på. 
git log: visar lista med alla som comittat o meddelandet
git log --oneline
git checkout (copy paste commits ID)
git checkout master
git stash (om man vill ogöra en grej man gjorde)
git stash pop (får tillbaks det man stashat. funkar innanman comittat)
"""
def interleave(seq1, seq2):
    new_seq = [] # det går ej att använda sånt på rekursion!!!!!!!!!!!
    if not seq1 or not seq2:
        return []
    if len(seq1) == len(seq2):
        new_seq.append(seq1[len(seq1)])#det går ej att använda append på rekursion!!!!!!!!!!!!!!!
    pass

def interlevae(seq1, seq2):
    if not (seq1 and seq2):
        return seq1 + seq2
    else:
        return [seq1[0], seq2[0]] + interleave(seq1[1:], seq2[1:])

# TDDD73 ------ EXEMPELTENTOR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
