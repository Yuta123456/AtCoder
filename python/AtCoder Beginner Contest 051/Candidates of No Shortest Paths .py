import copy
n, m = map(int ,input().split())
inf = 10**8
edges = []
graph = [[inf for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = graph[b][a] = c
    edges.append([a,b,c])
ans = 0
for i in range(n+1):
    graph[i][i] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
for i in range(m):
    flag = False
    a,b,c = edges[i]
    for j in range(1,n+1):
        for k in range(1,n+1):
            if graph[j][a] + c + graph[b][k] == graph[j][k]:
                flag = True
    if flag:
        ans += 1
print(m-ans)
