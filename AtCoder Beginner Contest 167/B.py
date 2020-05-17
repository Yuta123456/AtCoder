a,b,c,k = map(int, input().split())
ans = 0
if k <= a:
    print(k)
elif k <= a+b:
    print(a)
else:
    print(a-(k-a-b))
