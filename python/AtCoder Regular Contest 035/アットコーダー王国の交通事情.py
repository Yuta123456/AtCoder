n,m = map(int, input().split())
cost = [[10**10 for j in range(n+1)] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = cost[b][a] = c
k = int(input())
for i in range(1, n+1):
    cost[i][i] = 0
for p in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost[i][j] = min(cost[i][j], cost[i][p] + cost[p][j])
for _ in range(k):
    x, y, z = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost[i][j] = min(cost[i][j], cost[i][x] + cost[y][j] + z, cost[i][y] + cost[x][j] + z)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            ans += cost[i][j]
    print(ans)



    