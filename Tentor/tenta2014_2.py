"TENTA 2014, 2, 24 Oktober 2017" "3+2+3+"

##################################################################################
##################################################################################
"UPPGIFT 1"
"Deluppgift 1a" "OK" "3p"

def ascending(string):
    """
    Given a string, the function shall return a straight growing sequence av
    letters (also a string)
    """ #FRÅGA: coloca ponto final depois da docstrings?
    final_str = ""
    biggest_letter = string[0]
    final_str += string[0]
    for letter in string[1:]:
        if letter > biggest_letter.lower():
            final_str += letter
            biggest_letter = letter
    return final_str


"Deluppgift 1b" "n saiu"

def decode(seq):
    """
    Takes a string with words and applies function 'ascending()' to every word
    and returns the total result as a new string, that is the decoded message.
    """
    words = seq.split(' ') ### APRENDI: esse split() era oq me faltava pra resolver
    result = ""
    for word in words:
        result += ascending(word)
    print (words)
    return result

#################################################################################
#################################################################################
"UPPGIFT 2"
values = [[3, 2, 3, 3, 4, 3, 2, 3, 4], [], [6, 5, 6, 7, 8], [-2],  
            [5, -2, 5, 3, 0, 4, 3], [], [4, 6, 0, 2, -3]] 

"esse n saiu"
def remove_empty_r(series):
    """
    Recursive function that removes the empty lists within the big list that is 
    given (values).
    """
    if not series:
        return []
    elif not series[0]: #n entendi como isso pode funcionar
        return remove_empty_r(series[1:])
    else:
        return [series[0]] + remove_empty_r(series[1:])

"esse saiu" "2p"
def remove_empty_i(series):
    """
    Iterative function that removes the empty lists within the big list that is 
    given (values).
    """
    final_series = []
    for seq in series:
        if seq:
            final_series.append(seq)
    return final_series


#################################################################################
#################################################################################
"UPPGIFT 3"
"Deluppgift 3a" "OK!"

def with_series2(series, fn_check, fn_series):
    """
    Function that takes a series and two functions as arguments. The function
    shall treat the series given according to some pattern given by the functions,
    and return a list.
    """
    final_list = []
    for seq in series:
        if fn_check(seq):
            final_list += [fn_series(seq)]
    return final_list


"Deluppgift 3b" "saiu mais ou menos, olhei resposta"
 
def averages2(series, min_number):
    """
    The function shall return a list where all the numbers in a list's (series) 
    lists are bigger then min_number, and then return the average of the numbers
    in that list. Returns a list with the averages.
    """
    return with_series(values, (lambda seq: seq and all([x > 2 for x in seq])), \ 
                         lambda seq: sum(seq)/(len(lst)))
#APRENDI: all(...) returns True when all are True ([True,True,True]) 
# e tbm, sum(lista) que devolve a soma de todos elementos da lista.
    

#################################################################################
#################################################################################
"UPPGIFT 4"
"Deluppgift 4a"

def max_level(seq):
    """
    The function returns a number that corresponds to the number of levels
    existant in the list given as argument.
    """
    if not seq:
        return 0
    elif isinstance(seq[0], list):
        return max_level(seq[0]) + max_level(seq[1:]) 
    pass



    
