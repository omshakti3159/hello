

t=int(input())
while t:
    x=int(input())
    y=int(input())
    z=int(input())
    if y<x and z>x:
        print("PIZZA")
    elif z<x and y>x:
        print("BURGER")
    else:
        print("NOTHING")
    t-=1