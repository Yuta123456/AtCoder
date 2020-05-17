H,W = map(int, input().split())
num = []
s_x = -1
s_y = -1
g_x = -1
g_y = -1
locate_list = [[] for i in range(12)]
for i in range(H):
    k = list(input())
    if 'S' in k:
        s_y = i
        s_x = k.index('S')
        k[s_x] = 0
    if 'G' in k:
        g_y = i
        g_x = k.index('G')
        k[g_x] = 10
    k = list(map(int, k))
    for j in range(W):
        locate_list[int(k[j])].append([i,j])
    num.append(k)
ans = 0
adjacent_list = [[] for i in range(H*W)]
from heapq import heappush, heappop
def dijkstra(start,graph):
    INF = 10 ** 9
    global H
    global W
    dist = [INF] * (H*W)
    dist[start] = 0
    q = [(0,start)]
    while q:
        d,v = heappop(q)
        if dist[v] < d:
            continue
        for w,a in graph[v]:
            d1 = d + a
            if dist[w] > d1:
                dist[w] = d1
                heappush(q, (d1,w))
    return dist
#このまま適当にはって使える感じではない?
#隣接リスト適当に渡せば動く。重みを追加するのをわすれずに
for i in range(H):
    for j in range(W):
        for n_y,n_x in locate_list[num[i][j]+1]:
            adjacent_list[i*W+j].append([n_y*W+n_x, abs(i-n_y) + abs(j-n_x)])
cost = dijkstra(s_y*W+s_x,adjacent_list)
if cost[g_y*W+g_x] == 10**9:
    print(-1)
else:
    print(cost[g_y*W+g_x])

