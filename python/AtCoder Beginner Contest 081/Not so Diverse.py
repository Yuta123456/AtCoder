#input
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))


count = {}
for i in range(n):
    if a[i] not in count:
        count[a[i]] = 0
    count[a[i]] += 1
ans = 0
value = list(count.values())
value.sort()
for i in range(max(len(value) - k, 0)):
    ans += value[i]
print(ans)
