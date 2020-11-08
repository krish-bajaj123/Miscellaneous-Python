a=str(input('enter a string'))
def palindrome(n):
    x=n
    for i in range(0,int(len(x)/2)):
        if (x[i]!=x[len(x)-i-1]):
            return False
    return True
f=palindrome(a)
print(f)
