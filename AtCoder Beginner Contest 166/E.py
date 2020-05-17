n = int(input())
a = list(map(int, input().split()))
dic = dict()
ans = 0
for i in range(n):
    k = i + 1 - a[i]
    if k in dic:
        ans += dic[k]
    k = a[i] + i + 1
    if k in dic:
        dic[k] += 1
    else:
        dic[k] = 1
print(ans)
