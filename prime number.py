j=int(input("enter a number"))
i=2
f=0
k=int(input("enter a number"))
counter=0
l=j
while j<=k:
    while i<=(j/2):
        if (j%i==0):
            f=1
        i=i+1
    if (f==0):
        """print(j,"is a prime number")"""
        counter=counter+1
    j=j+1
    f=0
print(counter,"total number of primes from",l,"to",k)  
