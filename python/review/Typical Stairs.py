n, m = map(int, input().split())
mod = 10**9 + 7
dp = [0 for i in range(n+1)]
for i in range(m):
    dp[int(input())] = -1
dp[0] = 1
for i in range(n):
    if dp[i] != -1:
        if dp[i+1] != -1:
            dp[i+1] += dp[i]
            dp[i+1] %= mod
        if i+2 <= n and dp[i+2] != -1:
            dp[i+2] += dp[i]
            dp[i+2] %= mod
print(dp[n])