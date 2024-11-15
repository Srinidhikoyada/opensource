t = int(input())
for x in range(0,t):
    n,m = map(int,(input().split()))
    if n>m:
        print(n-m)
    else:
        print(0)
