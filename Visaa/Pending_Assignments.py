X,Y,Z = map(int,input().split())
Total_time = X*Y
available_time = Z*24*60
if Total_time <= available_time:
    print("YES")
else:
    print("NO")
