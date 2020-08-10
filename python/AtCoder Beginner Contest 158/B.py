n,b,a = map(int, input().split())
ans = 0
tmp = a+b
ans += (n // tmp) * b
n -= (n//tmp) * tmp
ans += min(n,b)
print(ans)