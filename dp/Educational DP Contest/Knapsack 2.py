n, w = map(int, input().split())
data = []
v_sum = 0
inf = 10**12
for i in range(n):
    data.append(list(map(int, input().split())))
    v_sum += data[i][1]

dp = [[inf for i in range(v_sum+1)] for j in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
    weight, v = data[i-1]
    for j in range(v_sum+1):
        if j - v >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v] + weight)
        else:
            dp[i][j] = dp[i-1][j]
ans = 0
for i in range(v_sum+1):
    if dp[-1][i] <= w:
        ans = max(ans, i)
print(ans)