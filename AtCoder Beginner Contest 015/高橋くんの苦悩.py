w = int(input())
n, k = map(int, input().split())
dp = [[[0 for i in range(k+1)] for j in range(w+1)] for _ in range(n+1)]
#dp[i][j][k] := i番目までの品物、幅j以下、k個使ったときの最高ばりゅ。
for i in range(1,n+1):
    width, value = map(int, input().split())
    for j in range(w+1):
        for l in range(1,k+1):
        #i個目の品物を使う場合 
            if j - width >= 0:
                dp[i][j][l] = max(dp[i-1][j - width][l-1] + value, dp[i-1][j][l])
            else:
                dp[i][j][l] = max(dp[i-1][j][l],dp[i][j][l])
ans = 0
print(dp[n][w][k])
