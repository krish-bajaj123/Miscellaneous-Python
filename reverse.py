i="krish"
j=len(i)-1
k=0
n=""
while j>=0:
    while k<=j:
        n=n+i[k]
        k=k+1
    print(n)
    j=j-1
    n=""
    k=0
