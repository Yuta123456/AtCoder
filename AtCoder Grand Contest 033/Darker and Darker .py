from collections import deque
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
grid = []
graph = [[2000 for i in range(w)] for j in range(h)]
#x,y渡すと、（ｈ、ｗ）に入ってるかどうか判定
def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False

#graph => そこまでの距離を保存した二次元配列　grid=>与えられた迷路
def bfs(que):
    finished = set()
    while que:
        x , y, cost = que.popleft()
        if (x,y) not in finished and graph[y][x] > cost:
            finished.add((x,y))
            graph[y][x] = cost
            if check(y,x+1):
                que.append([x+1,y,cost+1])
            if check(y+1,x):
                que.append([x, y+1, cost+1])
            if check(y,x-1):
                que.append([x-1,y,cost+1])
            if check(y-1,x):
                que.append([x,y-1,cost+1])
for i in range(h):
    grid.append(list(input()))
que = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            que.append((j,i,0))
bfs(que)
ans = 0
for i in range(h):
    ans = max(ans, max(graph[i]))
print(ans)