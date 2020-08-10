n, a = map(int, input().split())
x = list(map(int, input().split()))
#dp[i][j] := iの数字まで考えたとき、jの数字になる個数
max_s = sum(x)
dp = [[[0 for i in range(max_s + 1)] for j in range(n+1)] for k in range(len(x) + 1)]
#init
dp[0][0][0] = 1
dp[1][0][0] = 1
for i in range(1,n+1):
    num = x[i-1]
    for j in range(len(x)+1):
        for k in range(max_s + 1):
            if k - num < 0:
                dp[i][j][k] = dp[i-1][j][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k-num]
ans = 0
for i in range(len(x)+1):
    if i * a <= max_s+1:
        ans += dp[-1][i][i*a]
print(ans-1)
