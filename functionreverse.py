def reverse(i,word):
    j=len(i)
    k=len(word)
    x=0
    y=0
    flag=0
    while x<j:
        if (i[x]==word[0]):
            while(k>y):
                if(i[k]==" ")and(i[k]!=word[y]):
                    break
                k=k-1
                y=y+1
            else:
                flag=1
        x=x+1
    if(flag==1):
        return True
    else:
        return False


