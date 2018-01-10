"SEMINARIE 8"
# interpreterat språk (interpretator tex Python, Java Script): översätter sad för rad (tolk)
# + debuggning kan vara enklare att implementera
# + ingen kompilering behövs
# + om mnan har källkoden funkar det var som helst (mac, windows, ...)
# - långsam (speciellt för stora program)
# - källkod bevaras ej hemligt, det syns

# kompilerat språk (kompilator tex C++): översätter hela språket, maskinkod
# + snabba
# + ofta kan köras direkt utan å ladda ner stuff
# + fel upptäcks även innan man kör programmet
# - tar tid att kompilera

# S = a, aaa, aab, ba, bb

def check_1(string):
    lan1 = ['a', 'aaa', 'aab','ba', 'bb']
    if string in lan1:
        return True
    else: 
        return False

def check_letters(string):
    for letter in string:
        if letter not in 'ab':
            return False
    return True

def check_2(string):
    if string == string[::-1] and check_letters(string):
        return True
    else:
        return False


########################################################################



    
