import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

n, m = map(int, input().split())
graph = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = c
graph = dijkstra(csr_matrix(graph))
ans = 10**9
for i in range(n):
    ans = min(ans, max(graph[i]))
print(int(ans))