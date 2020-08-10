n = int(input())
h = list(map(int ,input().split()))
dp = [0 for i in range(n)]
h.reverse()
count = 0
for i in range(n - 1):
    if h[i + 1] >= h[i]:
        count += 1
        dp[i] = count
    else:
        count = 0
        dp[i] = count
print(max(dp))
