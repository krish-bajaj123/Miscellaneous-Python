f=open("ryu.txt")
j=open("kak.txt")
h=open("kri.txt","w")
for line1 in f:
    line2=j.readline()
    h.write(line1+line2)
h.close()
f.close()
j.close()
        
