from collections import deque
import sys
input = sys.stdin.readline
h,w = map(int, input().split())
grid = []
def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False
start = 0
goal = 0
for i in range(h):
    grid.append(list(input()))
for i in range(h):
    for j in range(w):
        if grid[i][j] == 's':
            start = (i,j)
        if grid[i][j] == 'g':
            goal = (i,j)
def bfs(y,x):
    que = deque([(y,x)])
    dist = [[4 for i in range(w)] for j in range(h)]
    dist[y][x] = 0 
    while que:
        y, x = que.popleft()
        for n_x, n_y in [(x+1,y), (x,y+1), (x-1,y),(x,y-1)]:
            cost = dist[y][x]  
            if check(n_y,n_x):
                if grid[n_y][n_x] == '#':
                    cost += 1
                if cost < dist[n_y][n_x] and cost <= 2:
                    que.append([n_y,n_x])
                    dist[n_y][n_x] = cost
    return dist
dist = bfs(*start)
if dist[goal[0]][goal[1]] <= 2:
    print("YES")
else:
    print("NO")