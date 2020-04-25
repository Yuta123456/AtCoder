s = input()
t = input()

n = len(s)
dp = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1] == t[j-1]:
            x = 1
        else:
            x = 0
        dp[i][j] = max(dp[i-1][j-1] + x, dp[i-1][j], dp[i][j-1])
print(dp[-1][-1] + 1)