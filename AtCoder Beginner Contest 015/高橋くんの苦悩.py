w = int(input())
n, k = map(int, input().split())
data = []
dp = [[[0,0] for i in range(w+1)] for j in range(n+1)]
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x:x[1])
data.reverse()
for i in range(1,n+1):
    weight, val = data[i-1]
    for j in range(1,w+1):
        if j - weight >= 0:
            if dp[i - 1][j][0] < dp[i-1][j-weight][0] + val and dp[i-1][j-weight][1] < k:
                dp[i][j] = [dp[i-1][j-weight][0] + val, dp[i-1][j-weight][1] + 1]
            else:
                dp[i][j] = dp[i-1][j]
print(dp[-1][-1][0])
