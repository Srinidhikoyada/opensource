X = int(input())
if X==0:
    print(1)
else:
    factorial = 1
    for i in range(1,X+1):
        factorial *= i
    ways = factorial 
    print(ways)
