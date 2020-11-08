list=[]
k=int(input("total number of elements"))
for i in range(k):
    j=int(input("enter a number"))
    list.append(j)
for i in range(k-1):
    for j in range(i+1,k):
        if(list[i]>list[j]):
            list[i]=list[i]+list[j]
            list[j]=list[i]-list[j]
            list[i]=list[i]-list[j]
print(list)
