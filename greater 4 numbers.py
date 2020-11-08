a,b,c,d=int(input("enter 4 numbers")),int(input()),int(input()),int(input())
if(a>b):
    if(a>c):
        if(a>d):
            print(a,"is te greatest number")
        else:
            print(d,"is the greatest number")
    elif(c>d):
        print(c,"is the greatest number")
elif(b>c):
    if(b>d):
        print(b,"is the greatest number")
    else:
        print(d,"is the greatest number")
else:
    if(c>d):
        print(c,"is the greatest number")
    else:
        print(d," is the greatest number")
