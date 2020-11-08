list=[1,2,3,4,5,6,7,8,9,76,54,98,63,45,90,86]
"""k=int(input("total number of elements"))
for i in range(k):
    j=int(input("enter a number"))
    list.append(j)"""
for i in range(len(list)-1):
    for j in range(i+1,len(list)):
        if(list[i]>list[j]):
            list[i]=list[i]+list[j]
            list[j]=list[i]-list[j]
            list[i]=list[i]-list[j]
print(list)
y=list
m=0
x=len(y)-1
mid=(m+x)//2
z=int(input("enter a number"))
while (True):
    if (y[mid]==z):
        print("found",z)
        break
    elif (y[mid]<z):
        m=mid
    else:
        x=mid
    if(m==x-1):
        if(y[m]==z)or(y[x]==z):
            print("found",z)
            break
        else:
            print("not found")
            break
    mid=(m+x)//2
    
    
