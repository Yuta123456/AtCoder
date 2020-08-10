n = int(input())
a = list(map(int, input().split()))
a.sort()
l = a[0]
r = a[-1]
ans = 10**10
for i in range(l,r+1):
    cand = 0
    for j in range(n):
        cand += (i - a[j])**2
    ans = min(ans, cand)
print(ans)