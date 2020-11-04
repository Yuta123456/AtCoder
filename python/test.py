s = list(input())
dp = [[0 for i in range(13)] for j in range(len(s)+1)]
mod = 10**9+7
dp[0][0] = 1
s.reverse()
ten_list = [0 for i in range(len(s)+1)]
ten_list[0] = 1         
for i in range(1,len(s) + 1):
    ten_list[i] = ( ten_list[i-1] * 10) % 13
for i in range(1,len(s)+1):
    ch = s[i-1]
    for j in range(13):
        dp[i][j] %= mod
        if ch == '?':
            for c_n in range(10):
                num = ( c_n * ten_list[i-1] ) % 13
                dp[i][(j+num)%13] += dp[i-1][j]
        else:
            num = ( int(ch) * ten_list[i-1] ) % 13
            dp[i][(j+num)%13] += dp[i-1][j]
print(dp[-1][5] % mod)
