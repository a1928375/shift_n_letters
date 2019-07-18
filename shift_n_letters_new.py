def rotate(a,b):
    L=[]
    if b>26:
        b-((b//26)*26)
    if b<26:
        b+((b//26)*26)
        
    for i in a:
        if ord(i)==32:
            L.append(i)
        else:
            c=ord(i)+b
            if c>122:
                c=c-26
            if c<97:
                c=c+26
            L.append(chr(c))
            
    string_new="".join(L)
    return string_new


print rotate ('sarah', 13)

print rotate('fnenu',13)

print rotate('dave',5)

print rotate('ifaj',-5)

print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu sv rscv kf ivru kyzj"),-17)
