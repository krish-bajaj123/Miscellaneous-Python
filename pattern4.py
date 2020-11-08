i=input("enter your name")
j=len(i)
k=0
l=""
sp=""
m=1
while k<j:
    while m<j-k:
        sp=" "+sp
        m=m+1
    m=1
    if (k==0):
        l=i[k]+l
    else:
        l=i[k]+l+i[k]
    k=k+1
    print(sp+l)
    sp=""
