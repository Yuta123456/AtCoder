import math
from scipy.sparse.csgraph import shortest_path
#道がない場合、infで初期化したい
inf = 10 ** 9 + 1
#input
n, m, l =list(map(int, input().split()))
way = [[inf for i in range(n)] for j in range(n)]
oil = [[inf for i in range(n)] for j in range(n)]

for i in range(m):
    a, b, c, = list(map(int, input().split()))
    way[a - 1][b - 1] = c
    way[b - 1][a - 1] = c
    if c <= l:
        oil[a - 1][b - 1] = 1
        oil[b - 1][a - 1] = 1

q = int(input())

query = []

for i in range(q):
    query.append(list(map(int, input().split())))

#ワーシャルフロイド法を使い、各道への最短経路を調べる。計算量はO(N**3)
for i in range(n):
    for j in range(n):
        for k in range(n):
            way[i][k] = min(way[i][k],way[i][j] + way[j][k])
            if i == k:
                way[i][k] = 0
#oilの補給できる回数もワーシャルフロイドで求める。これは補給可能な数,最小値が求まるらしい。よくわからん
for i in range(n):
    for j in range(n):
        for k in range(n):
            if oil[i][k] != inf:
                if way[i][k]

for i in range(q):
    ans = oil[query[i][0] - 1][query[i][1] - 1] - 1
    if way[query[i][0] - 1][query[i][1] - 1] == inf:
        ans = -1
    print(ans)












#aaaaa
