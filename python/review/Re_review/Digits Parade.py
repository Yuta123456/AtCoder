s = list(input())
s.reverse()
n = len(s)
mod = 10**9+7
#dp[i][j] := 下からi桁目まで決めたとき、13で割った余りがjの個数
dp = [[0 for i in range(13)] for j in range(n+1)]
dp[0][0] = 1
cur = 1
for i in range(n):
    for j in range(13):
        char = s[i]
        if char == '?':
            for k in range(10):
                #i+1桁目をkにする
                tmp = (k * cur) % 13
                dp[i+1][(j + tmp) % 13] += dp[i][j]
                dp[i+1][(j + tmp) % 13] %= mod
        else:
            x = int(char)
            tmp = (x * cur) % 13
            dp[i+1][(j + tmp) % 13] += dp[i][j]
            dp[i+1][(j + tmp) % 13] %= mod
    cur = (cur * 10) % 13
print(dp[n][5])

