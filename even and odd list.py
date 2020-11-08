even=[]
odd=[]
n=int(input("enter number of elements"))
for i in range(1,n+1):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even list is",even)
print("odd list is",odd)
a=[]
b=[]
for j in even:
    if(j%6==0):
        a.append(j)
for k in odd:
    if(k%3==0):
        b.append(k)
print(a)
print(b)
