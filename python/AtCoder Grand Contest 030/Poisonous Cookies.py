a,b,c = map(int, input().split())
ans = 0
if a + b + 1 >= c:
    ans += c
    ans += b
else:
    ans += (a + b + 1)
    ans += b
print(ans)


