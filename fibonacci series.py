nterms=int(input("number of terms"))
a,b=0,1
i=0
while (a<nterms) and (b<nterms):
    print(a)
    print(b)
    a=a+b
    b=b+a
    i=i+1
    
