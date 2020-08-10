n = int(input())
a = list(map(int, input().split()))
ans = max(a)
a.sort(reverse = True)
index = 1
for i in range(n-2):
    ans += a[index]
    if i % 2 == 1:
        index += 1
print(ans)