n, m = map(int, input().split())
count = [0 for i in range(m)]
ans = 0
for i in range(n):
    s = list(map(int, input().split()))
    k = s[1:s[0] + 1]
    for j in k:
        count[j - 1] += 1
for i in range(len(count)):
    if count[i] == n:
        ans += 1
print(ans)
