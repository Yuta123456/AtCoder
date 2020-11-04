n = int(input())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))
dp = [[10**10 for i in range(pow(2,n))] for j in range(n)]
dp[0][1] = 0
for k in range(pow(2, n)):
    for i in range(n):
        for j in range(n):
            #i->jの都市に行くときのコスト
            src = city[i]
            target = city[j]
            dp[j][k | (1<<j)] = min(dp[j][k | (1<<j)], dp[i][k] + abs(target[0] - src[0]) + abs(target[1] - src[1]) + max(0, target[2] - src[2]))

ans = dp[0][pow(2,n)-1]
print(ans)
