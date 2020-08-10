n = int(input())
data = []
dp = [[0 for i in range(3)] for j in range(n)]
for i in range(n):
    data.append(list(map(int, input().split())))
dp[0][0] = data[0][0]
dp[0][1] = data[0][1]
dp[0][2] = data[0][2]
for i in range(1, n):
    for j in range(3):
        k = {j}
        set = {0, 1, 2} - k
        dp[i][j] = data[i][j] + max(dp[i - 1][k] for k in list(set))
print(max(dp[n - 1]))
