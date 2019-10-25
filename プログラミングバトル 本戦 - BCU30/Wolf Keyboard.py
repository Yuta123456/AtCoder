n, k = list(map(int, input().split()))
data = []
for i in range(n):
    data.append(int(input()))
data.sort()
ans = 0
for i in range(n - k):
    ans += data[i]
ans = sum(data) + ans
print(ans)
