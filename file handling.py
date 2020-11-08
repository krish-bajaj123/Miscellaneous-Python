f=open("abc.txt")
b=[]
for a in f:
    b.append(a)
f.close()
print(b)
