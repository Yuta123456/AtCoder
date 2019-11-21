s = input()
t = input()

#dp[i][j] => s[i], t[j]までの最長部分文字列

dp = [[""] * (len(t) + 1) for j in range(len(s) + 1)]
for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = "".join(dp[i - 1][j] + s[i - 1])
        else:
            #上か左の長いほうを入れる
            if len(dp[i][j-1]) < len(dp[i-1][j]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(dp[-1][-1])
