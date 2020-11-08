a={"name":"krish","age":17,"class":12,"height":6,"weight":70}
print(a)
a["class"]=15
print(a)
for x in a.keys():
    print(a[x])
    if isinstance(a[x],int):
        a[x]=a[x]+1
print(a)
