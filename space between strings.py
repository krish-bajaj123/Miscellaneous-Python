i=input("enter a name")
j=len(i)
k=0
sp=""
ns=0
while k<j:
    if(i[k]==" "):
        if(i[k+1]==" "):
            sp=sp
        else:
            sp=sp+i[k]
            ns=1
    else:
        if(k==0)or(ns==1):
            sp=sp+ i[k].upper()
            ns=0
        else:
            sp=sp+i[k]
    k=k+1
print(sp)

