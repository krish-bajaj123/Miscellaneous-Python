f=open("gus.csv")
b=[]
c=0
d=0
e=0
for a in f:
    b.append(a.split(","))
for x in b:
        if x[1].rstrip()=="Appreciation Call":
            c=c+1
        elif x[1].rstrip()=="CFS Call":
            e=e+1
        else:
            d=d+1
print("we recieved ",c, "appreciation calls")
print("we recieved ",e, "cfs calls")
print("we recieved ",d, "enquiry calls")

f.close()
