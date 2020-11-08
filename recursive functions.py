def fact(a):
    if(a>1):
        return(fact(a-1)*a)
    else:
        return(a)
f=fact(5)
print(f)
