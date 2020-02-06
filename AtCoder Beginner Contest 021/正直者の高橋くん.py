from heapq import heappush, heappop
def dijkstra(start, graph):
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
def dijkstra2(start, graph,k):
    INF = 10 ** 15
    mod = 7 + 10**9
    #dp[i] = iまでの町の最短経路の本数
    dp = [0 for i in range(n+1)]
    dp[start] = 1
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
            if d1 == k[w]:
                dp[w] += dp[v] 
                dp[w] %= mod
    return dp
n = int(input())
a, b = map(int, input().split())
m = int(input())
adjacent_list = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    adjacent_list[x].append([y,1])
    adjacent_list[y].append([x,1])
k = dijkstra(a, adjacent_list)
lll = dijkstra2(a,adjacent_list,k)
print(lll[b])