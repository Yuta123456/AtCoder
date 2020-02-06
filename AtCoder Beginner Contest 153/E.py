h, n = map(int, input().split())
inf = 10**12
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
dp = [[inf for i in range(h+1 + 10**4)] for j in range(n+1)]
for i in range(n):
    dp[i][0] = 0
for i in range(n):
    a, b = data[i]
    for j in range(h+1+10**4):
        if j - a >= 0:
            dp[i+1][j] = min(dp[i+1][j-a] + b, dp[i][j])
        else:
            dp[i+1][j] = min(b, dp[i][j])
print(dp[-1][h])