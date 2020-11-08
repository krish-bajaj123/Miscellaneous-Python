num=int(input("enter a number"))
k=""
while num>0:
    remainder=num%2
    num=num//2
    k=str(remainder)+k
print(k)
