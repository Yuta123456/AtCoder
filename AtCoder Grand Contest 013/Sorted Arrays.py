n = int(input())
a = list(map(int, input().split()))
ans = 0
if n <= 2:
    print(1)
    exit()
pre = a[1] - a[0]
i = 2
while i < n:
    if pre * (a[i] - a[i-1]) < 0:
        ans += 1
        pre = 0
        i += 1
        if i == n:
            break
    if a[i] != a[i-1]:
        pre = a[i] - a[i-1]
    i += 1
print(ans + 1)
