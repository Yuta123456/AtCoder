n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()
ans = 0
pre = -1
for i in range(n):
    start, end = data[i]
    if pre >= start:
        pre = max(end, pre)
    else:
        ans += 1
        pre = max(pre,end)
print(ans)

