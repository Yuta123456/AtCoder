import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
n, m = map(int, input().split())
graph = [[0 for i in range(n+1)] for j in range(n+1)]
adjacent_node = []
for i in range(m):
    a, b, l = map(int, input().split())
    if a == 1:
        adjacent_node.append([b,l])
    elif b == 1:
        adjacent_node.append([a,l])
    else:
        graph[a][b] = graph[b][a] = l
#print(graph)
graph = dijkstra(csr_matrix(graph))
#print(graph)
inf = 10**9
ans = inf
for i in range(len(adjacent_node)):
    start, d_1 = adjacent_node[i]
    for j in range(i+1, len(adjacent_node)):
        goal, d_2 = adjacent_node[j]
        #print("start :{}  goal :{}".format(start, goal))
        ans = min(ans, d_1 + graph[start][goal] + d_2)
if ans == inf:
    print(-1)
else:
    print(int(ans))