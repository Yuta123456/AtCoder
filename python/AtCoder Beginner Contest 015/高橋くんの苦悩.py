w = int(input())
n, k = map(int, input().split())
dp = [[[0]*(w+1) for j in range(k+1)] for _ in range(n+1)]
#dp[i][j][k] := i番目までの品物、幅j以下、k個使ったときの最高ばりゅ。
for i in range(1,n+1):
    width, value = map(int, input().split())
    for j in range(w+1):
        for l in range(1,k+1):
        #i個目の品物を使う場合 
            if j - width >= 0:
                dp[i][l][j] = max(dp[i-1][l-1][j - width] + value, dp[i-1][l][j])
            else:
                dp[i][l][j] = max(dp[i-1][l][j],dp[i][l][j])
ans = 0
print(dp[n][k][w])
