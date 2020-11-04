import sys
sys.setrecursionlimit(10**9)
n = int(input())
a = list(map(int, input().split()))
dp = [[-1 for i in range(n)] for j in range(n)]
# dp[l][r] := 残りがl,rの区間だった時の
# 次の手番の人 - 自分の人の得点
for i in range(n):
    dp[i][i] = a[i]
def cul(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    dp[l][r] = max(a[l] - cul(l+1, r) , a[r] - cul(l, r-1))
    return dp[l][r]
print(cul(0,n-1))