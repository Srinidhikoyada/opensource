X,Y,Z = map(int,input().split())
if Z < Y:
    print("0")
else:
    print((Z-Y)//X)
