i=int(input("enter number of rows"))
j=1
k=""
l=1
print(k)
sp=""
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
    
