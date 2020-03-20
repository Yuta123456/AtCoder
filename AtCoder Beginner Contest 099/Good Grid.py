n, c = map(int, input().split())
cost = []
grid = []
for i in range(c):
    cost.append(list(map(int, input().split())))
for i in range(n):
    grid.append(list(map(int, input().split())))
div_3 = [[0 for i in range(c+1)] for j in range(3)]
for i in range(n):
    for j in range(n):
        div_3[(i+j+2)%3][grid[i][j]-1] += 1
ans = 10**9
for zero in range(c):
    for one in range(c):
        for two in range(c):
            if len(set([zero,one,two])) <= 2:
                continue
            cand = 0
            #3で割った余りがone,zeroとかの色で決まっている状態
            cand += sum([div_3[0][i] * cost[i][zero] for i in range(c) if i != zero])
            cand += sum([div_3[1][i] * cost[i][one]  for i in range(c) if i != one])
            cand += sum([div_3[2][i] * cost[i][two]  for i in range(c) if i != two])
            ans = min(ans, cand)
print(ans)

