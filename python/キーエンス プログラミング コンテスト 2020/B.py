n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
ans = 0
prex = -1 * 10**10
data.sort()
for i in range(n):
    x, l = data[i]
    if prex <= x - l:
        prex = x + l
    else:
        ans += 1
        prex = min(prex, x+l)
print(n-ans)