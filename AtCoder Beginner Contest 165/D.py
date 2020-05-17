def fn(x):
    return ((a*x)//b) - a*(x//b)
a,b,n = map(int, input().split())
ans = 0
if b <= n:
    ans = b-1
else:
    ans = n
print(fn(ans))