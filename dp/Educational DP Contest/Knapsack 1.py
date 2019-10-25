n, W = list(map(int, input().split()))
w = [0 for i in range(n)]
v = [0 for i in range(n)]
for i in range(n):
    w[i], v[i] = list(map(int, input().split()))
dp = [[0 for i in range(W + 1)] for j in range(n)]
for j in range(W+1):
    for i in range(n):
        p = j - w[i]
        s = dp[i - 1][j]
        if p >= 0:
            dp[i][j] = max(s, dp[i - 1][p] + v[i])
        else:
            dp[i][j] = s
print(dp[-1][-1])
