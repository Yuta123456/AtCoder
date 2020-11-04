n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
#dp[i][j] := i人目まで決め、キャンディをj個つかっているときの場合の数
dp = [[0 for i in range(k+1)] for j in range(n+1)]
dp[0][0] = 1
a.sort()
for i in range(n):
    acc = [0 for i in range(k+1)]
    for j in range(k+1):
        if dp[i][j] == 0:
            break
        acc[j] += dp[i][j]
        if j + a[i] + 1 <= k:
            acc[j + a[i] + 1] -= dp[i][j]
    dp[i+1][0] = acc[0]
    for j in range(1,k+1):
        acc[j] += acc[j-1]
        acc[j] %= mod
        dp[i+1][j] += acc[j]
        dp[i+1][j] %= mod
    #print(acc)
print(dp[n][k] % mod)