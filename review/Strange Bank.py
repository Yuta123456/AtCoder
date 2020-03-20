n = int(input())
inf = 10**9
dp = [inf for i in range(n+1)]
dp[0] = 0
for i in range(n):
    if dp[i] != inf:
        #1円引き出す場合
        dp[i+1] = min(dp[i] + 1, dp[i+1])
        num = 6
        while i + num <= n:
            dp[i + num] = min(dp[i] + 1, dp[i+num])
            num *= 6
        num = 9
        while i + num <= n:
            dp[i + num] = min(dp[i] + 1, dp[i+num])
            num *= 9

print(dp[n])
