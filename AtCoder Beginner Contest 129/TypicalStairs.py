N, M = map(int,input().split())
data = []
dp = ['.' for i in range(N + 1)]
dp[0] = 1
dp[1] = 1
for i in range(M):
    k = int(input())
    data.append(k)
    dp[k] = 0
mod = 10**9 + 7
for i in range(2,N + 1):
    if dp[i] != 0:
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
print(dp[N] % mod)
