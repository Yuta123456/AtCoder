import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
inf = (10.0) ** 10
n, m = list(map(int, input().split()))
#infを初期化
graph = np.full((n+1,n+1), inf)
#重み0の辺を追加(0にすると、辺が存在しないことになるため、小さい数を代入)
for i in range(1,n+1):
    graph[i][i - 1] = 0.0001
#辺の追加、重い辺は追加する必要がないため、小さいほうを採用
for i in range(m):
    l, r, c = list(map(int, input().split()))
    graph[l][r] = min(graph[l][r],  c)
    graph[r][l] = min(graph[r][l],  c)
graph = dijkstra(csr_matrix(graph))
#道がないなら‐１
if graph[1][n] == inf:
    print(-1)
else:
    print(int(graph[1][n]))