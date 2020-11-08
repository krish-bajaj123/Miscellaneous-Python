a,b,c=int(input("enter 3 numbers")),int(input()),int(input())
if(a>b):
    if(a>c):
        print("greatest number is",a)
    else:
        print("greatest number is",c)
elif(b>c):
    print("greatest number is",b)
else:
    print("greatest number is",c)
    
