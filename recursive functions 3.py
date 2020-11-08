def fib(n):
    if (n==0)or(n==1):
        return n
    else:
        r=fib(n-1)+fib(n-2)
        return r
terms=int(input("enter an integer"))
for i in range(terms):
    f=fib(i)
    print(f)
