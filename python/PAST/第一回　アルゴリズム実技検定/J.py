from collections import deque
h,w = map(int, input().split())
grid = []
n = h*w
adjacent_list =[[] for i in range(h*w+1)]
for i in range(h):
    grid.append(list(map(int, input().split())))
def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False
delta = [(-1,0),(1,0),(0,1),(0,-1)]
for i in range(h):
    for j in range(w):
        for dx,dy in delta:
            if check(i+dy,j+dx):
                #(i,j) -> (i+dy, j+dx)に辺をつなぐ
                adjacent_list[i*w+j].append([(i+dy)*w + (j+dx),grid[i+dy][j+dx]])
from heapq import heappush, heappop
def dijkstra(start,graph):
    INF = 10 ** 15
    dist = [INF] * (n+1)
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
#中間地点の全探索
ans = 10**9
start_to = dijkstra((h-1)*w,adjacent_list)
vie_to = dijkstra(h*w-1,adjacent_list)
goal_to = dijkstra(w-1,adjacent_list)
for i in range(h):
    for j in range(w):
        ans = min(ans, start_to[i*w+j] + vie_to[i*w+j] + goal_to[i*w+j] - grid[i][j]*2)
print(ans)