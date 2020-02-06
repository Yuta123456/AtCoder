import numpy as np
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def dijkstra(start, mode):
    INF = 10 ** 15
    dist = [INF] * (n+1)
    dist[start] = 0
    q = [(0,start)]
    while q:
        d,v = heappop(q)
        if dist[v] < d:
            continue
        for w,*a in graph[v]:
            d1 = d + a[mode]
            if dist[w] > d1:
                dist[w] = d1
                heappush(q, (d1,w))
    return dist

n,m,s,t = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    u,v,a,b = map(int, input().split())
    graph[u].append([v,a,b])
    graph[v].append([u,a,b])
money = dijkstra(s,0)
snu = dijkstra(t,1)
start = 10**15
#何年目か？
ans = []
ans_max = 10**15
for j in range(n,-1,-1):
    ans_max = min(ans_max, (money[j] + snu[j]))
    ans.append(ans_max)
for i in range(n-1,-1,-1):
    print(int(start - ans[i]))