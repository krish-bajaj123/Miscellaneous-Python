sum=0
l=int(input("enter a number"))
m=int(input("enter a number"))
while l<=m:
    j=l
    while j>0:
        e=j%10
        sum=sum+e**3
        j=j//10
    if (sum==l):
        print("sum is",sum,"hence",l,"is an armstrong number")
    sum=0
    l=l+1
    
