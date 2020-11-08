x=[[[],[]],[[],[]]]
for p in range(len(x)):
    for m in range(len(x[p])):
        for s in range(2):
            x[p][m].append(int(input("enter a number")))
for i in range(len(x)):
    for j in range(len(x[i])):
        for k in range(len(x[i][j])):
            print(x[i][j][k],end=" ")
        print("")
    print("")
