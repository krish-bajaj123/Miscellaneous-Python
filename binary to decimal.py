k=input()
j=len(k)
i=0
x=0
l=int(k)
while i<j:
    x=x+l%10*2**i
    l=l//10
    i=i+1
print(x)
    
    
