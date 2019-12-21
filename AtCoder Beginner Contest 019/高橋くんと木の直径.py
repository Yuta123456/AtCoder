n = int(input())
a = list(map(int, input().split()))
a.sort()
k = set(a)
ans = 0
for i in range(n):
    if a[i] in k:
        ans += 1
    if 2 * a[i] in k:
        k.remove(2 * a[i])
print(ans)