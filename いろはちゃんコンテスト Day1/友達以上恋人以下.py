n,m,k = map(int, input().split())
a = list(map(int, input().split()))
dp = [[-1 for i in range(m+1)] for j in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        index = max(0,i-k)
        max_day = -1
        for p in range(index,i):
            max_day = max(max_day,dp[p][j-1])
        if max_day == -1:
            dp[i][j] = -1
        else:
            dp[i][j] = max_day + a[i-1]
print(dp)
ans = -1
for i in range(n-k+1,n+1):
    ans = max(ans, dp[i][m])
print(ans)