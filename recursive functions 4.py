def series(n):
    if(n>1):
        print(series(n-2))
        return n
    else:
        return n
f=series(11)
print(f)
