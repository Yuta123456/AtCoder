from collections import deque
h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
def check(s,t):
    if (0 <= s <= w - 1) and (0 <= t <= h - 1):
        return True
    else:
        return False
def bfs(que):
    finished = set()
    while que:
        x , y, cost = que.popleft()
        if (not check(x,y) ) or grid[y][x] == '#':
            continue
        if (x,y) not in finished:
            finished.add((x,y))
            graph[y][x] = cost
            que.append([x+1,y,cost+1])
            que.append([x, y+1, cost+1])
            que.append([x-1,y,cost+1])
            que.append([x,y-1,cost+1])
ans = 0
inf = 400

for i in range(h):
    for j in range(w):
        que = deque()
        que.append([j,i,0])
        graph = [[inf for _ in range(w)] for _ in range(h)]
        bfs(que)
        for p in range(h):
            for q in range(w):
                if graph[p][q] < inf:
                    ans = max(ans, graph[p][q])
print(ans)