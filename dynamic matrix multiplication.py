x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,2,3],[4,5,6,7],[8,9,2,3]]
result=[[],[],[]]
r=0
"""for p in range(len(x)):
    for m in range(3):
        x[p].append(int(input("enter a number")))
for p in range(len(y)):
    for m in range(4):
        y[p].append(int(input("enter a number")))"""
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            r=r+x[i][k]*y[k][j]
        result[i].append(r)
        r=0
for r in result:
    print(r)
    

