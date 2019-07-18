def shift_n_letters(letter, n):
    L=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],["a", "b", "c", "d", "e", "f", "g", \
    "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]]
    i=0
    if n>26:
        n=n-((n//26)*26)
    if n<26:
        n=n-((n//26)*26)
        
    while True:
        if letter == L[1][i]:
            a=L[0][i]
            break
        else:
            i=i+1
    b=a+n
    if b>25:
        b=b-26
    if b<0:
        b=b+26    
    j=0
    while True:
        if b == L[0][j]:
            c=L[1][j]
            return c
        else:
            j=j+1

print shift_n_letters('s', 1)

print shift_n_letters('s', 2)

print shift_n_letters('s', 10)

print shift_n_letters('s', -10)
