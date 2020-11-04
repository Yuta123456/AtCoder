n, k = map(int, input().split())
span = []
mod = 998244353
for i in range(k):
    span.append(list(map(int, input().split())))
dp = [0 for i in range(n+1)]
acc = [0 for i in range(n + 1)]
dp[0] = 1
for i in range(n+1):
    acc[i] += acc[i-1]
    acc[i] %= mod
    dp[i] += acc[i]
    for j in range(k):
        l, r = span[j]
        if l + i < n + 1:
            acc[l + i] += dp[i]
        if r + 1 + i < n + 1:
            acc[r+1 + i] -= dp[i]
    dp[i] %= mod
print(dp[-2] % mod)