"TENTA 2014, 1" "2+3+5 = 10 = inte godkänd"

####################################################################################
"UPPGIFT 1"
"Del 1a"  "OK!" 

def find_notes(string):
    """
    Function that takes a string as argument, and returns another string that
    consists of letters that represents musical tones (CDEFGAH).
    """
    #FRÅGA: hur gör man en bättre doctrings? Finns inte det nån mall å följa?
    #FRÅGA: hur kan man hålla koll på att det inte överskrider 79 tecken?
    NOTES = "cdefgah" #FRÅGA: ska detta vara i stora bokstäver eller CamelCase eller?
    string_of_notes = ""
    for letter in string.lower():
        if letter in NOTES:
            string_of_notes += letter
    return string_of_notes

"Del 1b"   "NOT done"

def print_notes(string_of_notes):
    """
    Function that takes a string as argument that consists of only letters within
    "cdefgah", and that prints it a more simple and easy-to-see notesystem. 
    """
    notes = "cdefgah"
    if notes:
        for letter in string_of_notes:
            if letter == notes[-1]:
                print(letter)
            else:
                print(".")
            notes = notes[:-1] #vi exkluderar sista bokstaven

###################################################################################
"UPPGIFT 2"
"OK!"
def merge_r(seq_one, seq_two):
    """
    Recursive function that merges and then orders both lists that it takes as 
    arguments, and then returns a new ordered list.
    """
    if seq_one and seq_two:
        if seq_one[0] < seq_two[0]:
            return [seq_one[0]] + merge_r(seq_one[1:], seq_two)
        if seq_two[0] < seq_one[0]:
            return [seq_two[0]] + merge_r(seq_one, seq_two[1:])
    if seq_one and not seq_two:
        return [seq_one[0]] + merge_r(seq_one[1:], seq_two)
    if seq_two and not seq_one:
        return [seq_two[0]] + merge_r(seq_two[1:], seq_one)
    else: 
        return []
    
"NOT done yet"
def merge_i(seq_one, seq_two):
    """
    Iterative function that merges and then orders both lists that it takes as 
    arguments, and then returns a new ordered list.
    """
    pass
#while är också en iterativ grej

###################################################################################
"UPPGIFT 3"

"Deluppgift 3a"  "OK!"
#lärde mig: se n der rekursivt vai de iterativt.
#att skissa nånting på papper hjälper att tänka rätt. ha alltid penna o papper
# när du märker att uppgiften kräver lite mer fundering

def insert(inserted_element, seq, func):
    """
    Function that takes an element, a sorted list, and a sorting function as 
    arguments. It inserts the element in the list according to the function,
    and returns a list sorted according to the function.
    """
    #if not seq:
     #   return []
    #if func(element, seq[0]):
     #   return [element, seq[0]] + insert(element, seq[1:], func)
    #else:
     #   return [seq[0]] + insert(element, seq[1:], func)

    new_seq = []
    for list_element in seq:
        if func(inserted_element, list_element) and inserted_element not in new_seq:
            new_seq.append(inserted_element)
            new_seq.append(list_element)
        else:
            new_seq.append(list_element)
    return new_seq

"Deluppgift 3b" "OK!"

def insert_abs(element, seq):
    """
    Sorts a number in a list where the numbers come in an increasing order
    according the numbers absolut value.
    """
    return insert(element, seq, lambda x, y: abs(x) < abs(y))


def insert_seq(lst, lst_of_lsts):
    """
    Sorts a list (lst) in a list of lists (lst_of_lsts) decreasingly according
    to the length of the lists.
    """
    return insert(lst, lst_of_lsts, lambda x, y: len(x) > len(y))


####################################################################################
"UPPGIFT 4"

def longest_sequenceff(seq):
    """
    Functions that goes through all the elements of a given list and returns a 
    tuple consistant of the number that has the longest sequence within the list,
    and how big that straight sequence is.
    """
    pass

####################################################################################
"UPPGIFT 5"
def descendants(person, tree):
    """
    Function that, given the name of a person and the person's family tree,
    returns all the person's descendants in a list.
    """
    pass

#############################################################################
#############################################################################
#############################################################################

"FACIT"

"1a OK"
"1b"
def print_notes_facit(str):
    for note in "hagfedc":
        line = ""
        for char in str:
            if char == note:
                line += note
            else:
                line += "."
        print(line)
"2 rekursiv OK"

def merge_r_facit(seq1, seq2):
    if not seq1:
        return seq2
    elif not seq2:
        return seq1
    elif seq1[0] < seq2[0]:
        return [seq1[0]] + merge_r_facit(seq1[1:], seq2)
    else:
        return [seq2[0]] + merge_r_facit(seq1, seq2[1:])
"2 iterativ did not do"
def merge_i_facit(seq1, seq2):
    res = []
    while seq1 and seq2:
        if seq1[0] < seq2[0]:
            res.append(seq1[0])
            seq1 = seq1[1:]
        else:
            res.append(seq2[0])
            seq2 = seq2[1:]
    res = res + seq1 + seq2
    return res

"3a OK"
"3b OK"
def insert_facit(element,seq, func):
    if not seq:
        return [element]
    elif func(seq[0], element):
        return [seq[0]] + insert(element, seq[1:], func)
    else:
        return [element] + seq

"4 did not do"
def longest_sequence(seq):
    def longest_sequence_help(seq, cur_elm, cur_cnt, tot_elm, tot_cnt):
        if not seq:
            if cur_cnt > tot_cnt:
                return cur_elm, cur_cnt
            else:
                return tot_elm, tot_cnt
        elif seq[0] == cur_elm:
            return longest_sequence_help(seq[1:], cur_elm, cur_cnt+1, tot_elm, tot_cnt)
        elif cur_cnt > tot_cnt:
            return longest_sequence_help(seq, seq[0], 0, cur_elm, cur_cnt)
        else:
            return longest_sequence_help(seq, seq[0], 0, tot_elm, tot_cnt)   
    return longest_sequence_help(seq, seq[0], 0, 'NONE', 0)

"5 did not do"
def descendants(person, table):
    result = []
    if person in table:
        children = table[person]
        result = list(children)
        for child in children:
            result += descendants(child, table)
    return result
