import sys
input = sys.stdin.readline
#道がない場合、infで初期化したい
inf = 10 ** 13 + 1
#input
n, m, l = list(map(int, input().split()))
way = [[inf for i in range(n)] for j in range(n)]
oil = [[400 for i in range(n)] for j in range(n)]

for i in range(m):
    a, b, c, = list(map(int, input().split()))
    way[a - 1][b - 1] = c
    way[b - 1][a - 1] = c

q = int(input())

query = []

for i in range(q):
    query.append(list(map(int, input().split())))

#ワーシャルフロイド法を使い、各道への最短経路を調べる。計算量はO(N**3)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                way[i][j] = 0
                continue
            way[i][j] = min(way[i][j],way[i][k] + way[k][j])
            
#oilの補給できる回数もワーシャルフロイドで求める。まず、一補給でいけるところに辺を張る
for i in range(n):
    for j in range(n):
        if i == j:
            oil[i][j] = 0
        if way[i][j] <= l:
            oil[i][j] = oil[j][i] = 1
#の後でワーシャルフロイド
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                oil[i][j] = 0
                continue
            oil[i][j] = min(oil[i][j],oil[i][k] + oil[k][j])

for i in range(q):
    ans = oil[query[i][0] - 1][query[i][1] - 1] - 1
    if way[query[i][0] - 1][query[i][1] - 1] >= inf or oil[query[i][0] - 1][query[i][1] - 1] == 400:
        ans = -1
    print(ans)
