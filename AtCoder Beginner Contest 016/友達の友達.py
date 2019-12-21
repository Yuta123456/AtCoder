import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix


n,m = map(int, input().split())
graph = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
#dfs
graph = dijkstra(csr_matrix(graph))
for i in range(1,n+1):
    k = list(graph[i])
    print(k.count(2))



