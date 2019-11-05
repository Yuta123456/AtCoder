import numpy as np
from scipy.sparse.csgraph import dijkstra
import itertools
from scipy.sparse import csr_matrix
inf = 1 + 10**8
n, m, r = list(map(int, input().split()))
r = list(map(int, input().split()))
graph = np.full((n+1,n+1), inf)
for i in range(m):
    a,b,c = list(map(int, input().split()))
    graph[a][b] = c
    graph[b][a] = c
p_list = list(itertools.permutations(r,len(r)))
graph = dijkstra(csr_matrix(graph))
min_cost = inf * 200
for i in p_list:
    candidate = 0
    for j in range(len(i) - 1):
        candidate += graph[i[j]][i[j + 1]]
    if min_cost > candidate:
        min_cost = candidate
print(int(min_cost))