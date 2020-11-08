x=[[[1,2,3],[3,4,5]],[[4,5,6],[6,7,8]]]
for i in range(len(x)):
    for j in range(len(x[i])):
        for k in range(len(x[i][j])):
            print(x[i][j][k],end=" ")
        print("")
    print("")
                   
