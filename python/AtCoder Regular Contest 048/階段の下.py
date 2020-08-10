a,b = map(int, input().split())
if a*b < 0:
    print(b-a-1)
else:
    print(b-a)