n, m, k = map(int, input().split())
from heapq import heappush, heappop
def dijkstra(start):
    INF = 10 ** 15
    dist = [INF] * (n+1)
    dist[start] = 0
    q = [(-1,start)]
    pre_jump = [set() for i in range(n+1)]
    while q:
        d,v = heappop(q)
        if dist[v] < d:
            continue
        for w,a in graph[v]:
            if a in pre_jump[v]:
                d1 = d
            else:
                d1 = d + 1
            if dist[w] > d1:
                dist[w] = d1
                pre_jump[w].add(a)
                heappush(q, (d1,w))
    return dist
#このまま適当にはって使える感じではない?
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
arr = dijkstra(1)
if arr[n] == 10**15:
    print(-1)
else:
    print((arr[n] + 1) * k)
