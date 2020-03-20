n, a = map(int, input().split())
x = list(map(int, input().split()))
#dp[i][j][k] := i枚目までカードを選び、合計がjになり、k枚カードを選んだ選び方の総数
#合計のマックスは、xの総和で考える、高々2500なので間に合う
dp = [[[0 for i in range(n+1)] for j in range(sum(x)+1)] for k in range(n+1)]
dp[0][0][0] = 1
for i in range(1,n+1):
    for j in range(sum(x) + 1):
        for k in range(n+1):
            if j + x[i-1] < sum(x) + 1 and k < n:
                dp[i][j + x[i-1]][k+1] += dp[i-1][j][k]
            dp[i][j][k] += dp[i-1][j][k]
ans = 0
for j in range(sum(x)+1):
    for k in range(1,n+1):
        if j == a * k:
            ans += dp[-1][j][k]

print(ans)