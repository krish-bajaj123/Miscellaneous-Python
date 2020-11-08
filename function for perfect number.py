n=int(input("enter an integer"))
def perfect(n):
    sum1=0
    for i in range(1,n):
        if(n%i==0):
            sum1=sum1+i
    if(sum1==n):
        print("the number is aperfect number")
    else:
        print("the number is not a perfect number")
f=perfect(n)
print(f)
