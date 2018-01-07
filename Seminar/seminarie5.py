"SEMINARIUM 5"

def pal_num(n):
    s = str(n)
    return s == s[::-1]

def fib_maker():
    a, b = 0, 1
    def next_fib():
        nonlocal a, b
        a, b = b, a + b
        return b - a
    return next_fib

def func(seq):
    res = []
    for elem in seq:
        if elem % 2 == 0:
            res.append(elem)
    return res

def func2(seq): # indexet ointressant. Använd det när du vill ändra seq[i] osv
    res = []
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            res.append(seq[i])
    return res
