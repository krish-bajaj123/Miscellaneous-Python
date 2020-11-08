a,b,c,d=int(input("enter 4 numbers")),int(input()),int(input()),int(input())
if(a<40):
    print(a,"is fail")
else:
    print(a,"is pass")
if(b<40):
    print(b,"is fail")
else:
    print(b,"is pass")
if(c<40):
    print(c,"is fail")
else:
    print(c,"is pass")
if(d<40):
    print(d,"is fail")
else:
    print(d,"is pass")
e=a+b+c+d
print(e,"is total marks out of 400")
f=e*0.25
if(f>=70):
    print(f,"% is a ")
elif(f>=50):
    print(f,"% is b")
elif(f>=30):
    print(f,"% is c")
else:
    print(f,"% is fail")
    
