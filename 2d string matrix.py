p=input("enter 9 number seperated by space")
a=[[0,0,0],[0,0,0],[0,0,0]]
n=0
m=0
j=len(p)
s=p[0]
for i in range(1,j):
    if(p[i]!=" "):
        s=s+p[i]
    else:
        a[m][n]=int(s)
        s=""
        if(n==(len(a[m])-1))and(m!=(len(a)-1)):
           m=m+1
           n=0
        else:
            n=n+1
a[m][n]=int(s)
for i in a:
    print(i)
    
