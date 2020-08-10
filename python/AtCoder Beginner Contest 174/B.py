n, d = map(int, input().split())
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    ans += int(pow(pow(x, 2) + pow(y, 2), 0.5) <= d)
print(ans)                      