"SEMINARIE 10"
"presentation labb8-almanacka"
"abstraktionslager" "-" "användbar när man skriver stora program"
"abstrakt, prmitiva"

def sum_all(seq):
    if not seq:
        return 0
    if isinstance(seq[0], list):
        return sum_all(seq[0]) + sum_all(seq[1:])
    else:
        return seq[0] + sum_all(seq[1:])
    
def sum_it(seq):
    sum = 0
    if isinstance
    for elem in seq:
        part = sum_all(elem)
        sum += part
    return sum

