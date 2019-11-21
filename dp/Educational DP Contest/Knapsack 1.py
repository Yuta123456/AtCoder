n, W = list(map(int, input().split()))
w = [0 for i in range(n + 1)]
v = [0 for i in range(n + 1)]
for i in range(n):
    w[i + 1], v[i + 1] = list(map(int, input().split()))
dp = [[0 for i in range(W+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,W+1):
        if w[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
print(int(dp[n][W]))