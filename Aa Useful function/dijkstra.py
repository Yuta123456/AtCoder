from heapq import heappush, heappop
def dijkstra(start):
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
#このまま適当にはって使える感じではない?
#隣接リスト適当に渡せば動く。重みを追加するのをわすれずに