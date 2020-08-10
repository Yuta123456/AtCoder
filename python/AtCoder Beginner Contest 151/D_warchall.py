h, w = map(int, input().split())
grid = []
inf = 400
for i in range(h):
    grid.append(list(input()))
graph = [[0 for i in range(h*w)] for j in range(h*w)]
for i in range(h):
    for j in range(1,w):
        u = i * w + j - 1
        v = i * w + j
        if grid[i][j-1] != '#' and grid[i][j] != '#':
            graph[u][v] = graph[v][u] = 1
for i in range(w):
    for j in range(1,h):
        u = (j - 1) * w + i
        v = j * w + i
        if grid[j-1][i] != '#' and grid[j][i] != '#':
            graph[u][v] = graph[v][u] = 1
distance = [[inf for i in range(h*w)] for j in range(h*w)]
for i in range(h*w):
    for j in range(w*h):
        if graph[i][j] == 1:
            distance[i][j] = 1
    distance[i][i] = 0
for k in range(h*w):
    for j in range(w*h):
        for i in range(w*h):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
ans = 0
for i in range(h*w):
    for j in range(h*w):
        if distance[i][j] != inf:
            ans = max(ans, distance[i][j])
print(ans)