def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
z=1
while(z>0)and(z<=4):
    x=int(input("enter a number"))
    y=int(input("enter a number"))
    z=int(input("enter a number"))
    if(z==1):
        add(x,y)
    elif(z==2):
        subtract(x,y)
    elif(z==3):
        multiply(x,y)
    elif(z==4):
        divide(x,y)
    else:
        break

    
