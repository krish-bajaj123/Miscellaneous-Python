i=input("enter the sentance")
word=input("enter the word")
j=len(i)
k=len(word)
x=0
y=0
flag=0
while x<j:
    if (i[x]==word[0]):
            while(y<k):
                if(i[x]==" ")and(i[x]!=word[y]):
                    break
                y=y+1
                x=x+1
            else:
                flag=1
    x=x+1
if(flag==1):
    print("true")
else:
    print("false")
                
                
            
        
   
