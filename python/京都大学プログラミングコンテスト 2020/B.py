from bisect import bisect_left
n, k = map(int, input().split())
dp = [[0 for i in range(k)] for j in range(n)]
array = []
mod = 10**9+7
for i in range(k):
    dp[0][i] = 1
for i in range(n):
    array.append(list(map(int, input().split())))
for i in range(n-1):
    acc = [0 for i in range(k)]
    for j in range(k):
        index = bisect_left(array[i+1], array[i][j])
        if index < k:
            acc[index] += dp[i][j]
    dp[i+1][0] += acc[0]
    for j in range(1,k):
        acc[j] += acc[j-1]
        dp[i+1][j] += acc[j]
        dp[i+1][j] %= mod
print(sum(dp[-1]) % mod)
