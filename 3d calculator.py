c,cu,cub=int(input()),int(input()),int(input())
if(c):
    r=int(input("radius of circle"))
    circle=3.14*r**2
    print(circle,"area of the circle")
elif(cu):
    a=int(input("side of square"))
    cube=a**3
    print(cube,"volume of the cube")
else:
    l=int(input("length of cuboid"))
    b=int(input("breadth of cuboid"))
    h=int(input("height of cuboid"))
    cuboid=l*b*h
    print(cuboid,"volume of the cuboid")


    
