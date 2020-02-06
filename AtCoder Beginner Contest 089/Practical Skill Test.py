import math
h, w, d = list(map(int, input().split()))
grid = []
num = [[] for i in range(h*w+1)]
for i in range(h):
    grid.append(list(map(int, input().split())))
for i in range(h):
    for j in range(w):
        num[grid[i][j]]=[j+1, i+1]
k = math.ceil((h*w+1) / d)
#initialize
cost = [[0 for i in range(k)] for j in range(d)]
for i in range(d + 1,h*w+1):
    x, y = num[i]
    prex, prey = num[i - d]
    cost[i % d][i//d] = abs(prex - x) + abs(prey - y)
    cost[i % d][i//d] += cost[i % d][(i - d)// d]
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(cost[r%d][r//d] - cost[l%d][l//d])
