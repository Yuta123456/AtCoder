n,ma,mb = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
#dp[i][j][k] := i番目まで考えたとき,薬品がjg, kgになる最小コスト
inf = 10**9
dp = [[[inf for i in range(n*11)] for j in range(n*11)] for k in range(n+1)]
for i in range(n):
    #0g, 0g にするためのコストは0
    dp[i][0][0] = 0
for i in range(1,n+1):
    typeA,typeB,cost = data[i-1]
    for j in range(n*11-typeA):
        for k in range(n*11-typeB):
            if dp[i][j+typeA][k+typeB] > dp[i-1][j][k] + cost:
                dp[i][j+typeA][k+typeB] = dp[i-1][j][k] + cost
            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
ans = inf
for i in range(1,n*11):
    for j in range(1,n*11):
        if i / j == ma / mb:
            #print("{} {} {}".format(i,j,dp[n][i][j]))
            ans = min(ans, dp[n][i][j])
if ans == inf:
    print(-1)
else:
    print(ans)