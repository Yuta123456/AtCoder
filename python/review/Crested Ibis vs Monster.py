h, n = map(int, input().split())
inf = 10**10
dp = [[inf for i in range(h+1)] for j in range(n+1)]
#dp[i][j] := i番目の魔法まで考えたとき、hpをh減らす最小コスト
dp[0][0] = 0
for i in range(1,n+1):
    damage, cost = map(int, input().split())
    for j in range(h+1):
        if j - damage < 0:
            dp[i][j] = min(cost, dp[i][j], dp[i-1][j])
        else:
            dp[i][j] = min(dp[i][j - damage] + cost, dp[i-1][j])
print(dp[-1][h])