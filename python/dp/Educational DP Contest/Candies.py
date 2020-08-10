n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
#dp[i][j] := i人目まで決め、キャンディをj個つかっているときの場合の数
dp = [[0 for i in range(k+1)] for j in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(a[i]+1):
        if dp[i][j] == 0:
            break
        for candy in range(a[i]+1):
            if j + candy < k+1:
                dp[i+1][j+candy] += dp[i][j]
                dp[i+1][j+candy] %= mod
print(dp[n][k])