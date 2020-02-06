n = int(input())
p = list(map(float, input().split()))
#dp[i][j] := i枚目のコインを投げ、表がj枚の確率 
#遷移式は、今回のコインが表が出るか、裏が出るかのみ考えればよい
dp = [[0 for i in range(n+1)] for j in range(n+1)]
dp[0][0] = 1.0
for i in range(1,n+1):
    k = p[i-1]
    for j in range(i+1):
        #さっきj枚達成してたら、裏じゃなきゃいけない
        #さっきはj-1しか達成できてないなら、今回は表
        if j > 0:
            dp[i][j] += (dp[i-1][j-1] * k) + (dp[i-1][j] * (1 - k))
        else:
            dp[i][j] += dp[i-1][j] * (1 - k)
ans = 0
for i in range(n+1):
    if (n - i) < i:
        ans += dp[-1][i]
print(ans)