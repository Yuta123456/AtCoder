n = list(input())
inf = 10**9
dp = [[inf for i in range(2)] for j in range(len(n) + 2)]
#dp[i][j] := 下からi桁目まで決めたときの、繰り下がりがjである。(true, false)
#ときの、最小紙幣数
n.reverse()
n += ['0']
#繰り下がりがない
dp[0][0] = 0
#配るDP
for i in range(len(n)):
    for j in range(2):
        x = int(n[i])
        #さっきの桁に繰り下がりをしている場合は、今回の数字が一つ減る。
        #んだけど、実際に払う数字は後で決めるから、今回は、引く側の数字を1大きく
        #することで、同じ操作を実現している
        x += j
        for a in range(10):
            #今回払う数字を決める
            if a >= x:
                #繰り下がりなし
                dp[i+1][0] = min(dp[i+1][0], dp[i][j] + 2 * a - x)
            else:
                #繰り下がりあり
                dp[i+1][1] = min(dp[i+1][1], dp[i][j] + 2 * a - x + 10)
print(min(dp[len(n)][0], dp[len(n)][1]))

