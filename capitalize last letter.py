i=input("enter a name")
j=len(i)
k=0
sp=""
ns=0
m=j-1
while k<j:
    if(i[k]!=" ")and(k!=m):
        if(i[k+1]==" "):
            sp=sp+ i[k].upper()
        else:
            sp=sp+i[k]
    else:
        if(k==m):
            sp=sp+ i[k].upper()
        elif(i[k+1]==" "):
            sp=sp
        else:
            sp=sp+i[k]
        
    k=k+1
print(sp)
