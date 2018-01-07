#List- o strängmetoder
#.append('hallon')
#L.insert(1,'blåbär') - lägger till bläbär i plats 1
#L.remove()
#L.sort() - sorterar efter nåt
#blankrader: max 1 blankrad/funktion, och 2 blankrader mellan funktioner.
#namn på fil: countimaginary.py (ingen understreck)
#konstanter: WINDOW_WIDTH (stora bokstäver, understreck)

def find_in_list(seq,needle):
    if not seq:
        #print('1',seq)
        return False
    elif isinstance(seq[0],list):
        #print('2',seq)
        return find_in_list(seq[0], needle)# or find_in_list(seq[1:], needle)
    elif seq[0] == needle:
        #print('3',seq)
        return True
    else:
        #print('4',seq)
        return find_in_list(seq[1:],needle)
