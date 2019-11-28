import numpy as np
n, m = map(int, input().split())
graph = np.zeros((n+1,n+1))
for i in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
start, goal = map(int, input().split())
graph2 = np.zeros((n+1,n+1))
np.dot(graph,graph,out = graph2)
np.dot(graph2,graph,out = graph)
#一回けんけんぱした後のグラフがgraph
for i in range(1,n+1):
    if graph[start][goal] >= 1:
        print(i)
        exit()
    np.dot(graph,graph,out = graph)
print(-1)