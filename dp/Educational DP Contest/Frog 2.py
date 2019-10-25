n, k = list(map(int, input().split()))
h = list(map(int, input().split()))
inf = 10 ** 4 + 1
dp = [inf] * n
dp[0] = 0
for i in range(1,n):
    H = h[i]
    dp[i] = min([dp[j] + abs(h[j] - H) for j in range(max(0, i - k), i)])
print(dp[-1])
