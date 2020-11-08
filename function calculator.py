def calculator(x,y):
    choice=int(input("enter a number from 1 to 4"))
    if choice==1:
        return(x+y)
    elif choice==2:
        return(x-y)
    elif choice==3:
        return(x/y)
    elif choice==4:
        return(x*y)
calculator(23,45)
