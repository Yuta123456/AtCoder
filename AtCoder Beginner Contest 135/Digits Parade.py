s = input()
#文字の昇順に処理していきたいため、逆順にしておく
s = s[::-1]
mod = 7 + 10**9
keta = 1
dp = [[0 for i in range(13)] for j in range(len(s) + 1)]
dp[0][0] = 1
for i in range(len(s)):
    if s[i] != "?":
        k = (int(s[i]) * keta) % 13
        for j in range(13):
            dp[i + 1][(j + k) % 13] = dp[i][j]
    else:
        for j in range(13):
            for k in range(10):
                l = ( k * keta ) % 13
                dp[i + 1][(j + l) % 13] += dp[i][j] % mod
    keta = keta *10 % 13 
print(dp[-1][5] % mod)
