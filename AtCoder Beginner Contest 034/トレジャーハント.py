n,m,t = map(int, input().split())
earn = list(map(int, input().split()))
adjacent_list_a = [[] for i in range(n+1)]
adjacent_list_b = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    adjacent_list_a[a].append([b,c])
    adjacent_list_b[b].append([a,c])
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
dist_a = dijkstra(1,adjacent_list_a)
dist_b = dijkstra(1,adjacent_list_b)
ans = 0
#滞在する頂点を全探索するから
for i in range(1,n+1):
    time = t - (dist_a[i] + dist_b[i])
    ans = max(ans, time*earn[i-1])
print(ans)

