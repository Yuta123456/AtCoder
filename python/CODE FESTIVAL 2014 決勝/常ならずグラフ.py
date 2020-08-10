n = int(input())
r = list(map(int, input().split()))
dp = [[0, 0] for i in range(n)]
dp[-1][0] = 1
dp[-1][1] = 1
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if r[j] > r[i]:
            dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        elif r[j] < r[i]:
            dp[i][1] = max(dp[i][1], dp[j][0] + 1)
ans = 0
for i in range(n):
    for j in range(2):
        ans = max(ans, dp[i][j])
if ans <= 3:
    print(0)
else:
    print(ans)