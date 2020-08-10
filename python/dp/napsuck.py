import numpy as np
n, w = list(map(int, input().split()))
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
dp = np.zeros((n + 1,w + 1))
for i in range(1,n):
    for j in range(1, w+1):
        if data[i][0] > j:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - data[i][0]] + data[i][1])
print(int(dp[n - 1][w]))
