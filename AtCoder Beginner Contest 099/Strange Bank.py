import bisect
n = int(input())
add_num = 1
draw_money = []
while add_num <= 10 ** 5:
    draw_money.append(add_num)
    add_num *= 6
    
add_num = 1
while add_num <= 10 ** 5:
    draw_money.append(add_num)
    add_num *= 9

#重複を削除
draw_money = list(set(draw_money))
ans = 0
draw_money.sort()
# dp[i] = i円引き出すのに必要な最小操作
dp = [10000000] * (n + 1)
dp[0] = 0
for i in range(1,n + 1):
    for j in draw_money:
        if  i - j >= 0:
            dp[i] = min(dp[i - 1] + 1, dp[i - j] + 1,dp[i])
        else:
            dp[i] = min(dp[i-1] + 1, dp[i])

print(dp[n])



