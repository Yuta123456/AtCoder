import sys
sys.setrecursionlimit(10**5)
s = input()
t = input()

#dp[i][j] => s[i], t[j]までの最長部分文字列

dp = [[0] * (len(t) + 1) for j in range(len(s) + 1)]
for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1] == t[j-1]:
            x = 1
        else:
            x = 0
        dp[i][j] = max(dp[i-1][j-1] + x, dp[i-1][j], dp[i][j-1])


def make_ans(a, b):
    if a ==  0 or b == 0:
        return 
    if s[a-1] == t[b-1]:
        make_ans(a-1,b-1)
        ans.append(s[a-1])
    else:
        if a == 0:
            make_ans(a, b - 1)
        elif b == 0:
            make_ans(a - 1,b)
        else:
            if dp[a - 1][b] > dp[a][b - 1]:
                make_ans(a-1,b)
            else:
                make_ans(a,b-1)

ans = []
make_ans(len(s),len(t))
print("".join(ans))