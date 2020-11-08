i=input("enter a name")
j=len(i)-1
k=0
sp=""
ns=0
p=""
n=0
while j>k:
    if(i[j]==" "):
        n=j
        break
    else:
        sp=i[j]+sp
    j=j-1
sp=sp.capitalize()
while k<n:
    if(k==0):
        p=p+ i[k].capitalize()+" "
    if((i[k]==" ")and(i[k+1]!=" ")):
        p=p+ (i[k+1]).upper()+" "
    k=k+1
print(p+sp)

        
        
        
    
    

