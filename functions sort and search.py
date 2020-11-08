list=[]
k=int(input("total number of elements"))
for i in range(k):
        j=int(input("enter a number"))
        list.append(j)
def sort(list):
    k=len(list)
    for i in range(k-1):
        for j in range(i+1,k):
            if(list[i]>list[j]):
                list[i]=list[i]+list[j]
                list[j]=list[i]-list[j]
                list[i]=list[i]-list[j]
    print(list)
def search(list):
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
sort(list)
search(list)
list1=[1,2,3,4,5,6,7,8,98,13,678,999]
sort(list1)
search(list1)
