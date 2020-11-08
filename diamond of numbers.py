i=int(input("enter number of rows"))
j=1
k=""
l=1
print(k)
sp=""
r=0
h=1
while j<=i:
    while l<=i-j:
        sp=" "+sp
        l=l+1
    l=1
    if (j==1):
        k=k+str(j)
    else:
        k=str(j)+k+str(j)
    print(sp+k)
    j=j+1
    sp=""
k=""
m=i
i=i-1
while i>=0:
    while r<m-i:
        sp=" "+sp
        r=r+1
    r=0
    while h<=i:
        if(h==1):
            k=k+str(h)
        else:
            k=str(h)+k+str(h)
        h=h+1
    print(sp+k)
    m=m-1
    i=i-1
    k=""
    h=1
