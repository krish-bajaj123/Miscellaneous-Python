def series(a):
    if(a>1):
        series(a-1)
        print(2**a)
    else:
        print(2**a)
f=series(5)
print(f)
