n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n-1):
    if x >= a[i]:
        x -= a[i]
        ans += 1
if x == a[-1]:
    ans += 1
print(ans)