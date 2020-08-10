n = int(input())
a = list(map(int, input().split()))
inf = 10**12
dp = [inf]*n
dp[0] = 0
dp[1] = abs(a[1] - a[0])
for i in range(2,n):
    dp[i] = min(dp[i], dp[i-1] + abs(a[i] - a[i-1]), dp[i-2] + abs(a[i] - a[i-2]))
print(dp[-1])