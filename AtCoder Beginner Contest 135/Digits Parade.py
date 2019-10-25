import numpy as np
k = input()
#文字の昇順に処理していきたいため、逆順にしておく
s = k[::-1]
dp = np.zeros((len(s), 13))
for i in range(len(s)):
    if s[i] == '?':
        for j in range(10):
            dp[i][j] += 
    else:
        for j in range(13):
            dp[i][j] += dp[i - 1][j - int(s[i])]
