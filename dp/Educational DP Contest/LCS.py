import sys
input = sys.stdin.readline

s = input()
t = input()

#dp[i][j] => s[i], t[j]までの最長部分文字列


dp = [[""] * (len(t) + 1) for j in range(len(s) + 1)]
for j in range(len(t)):
    for i in range(len(s)):
        if s[i] == t[j]:
            v =  [dp[i][j] + s[i], dp[i + 1][j],dp[i][j + 1]]
            v = sorted(v, key = lambda x:len(x))
        else:
            v = [dp[i + 1][j], dp[i][j + 1]]
            v = sorted(v, key = lambda x:len(x))
        dp[i + 1][j + 1] = v[-1]
print(dp[-1][-1])
