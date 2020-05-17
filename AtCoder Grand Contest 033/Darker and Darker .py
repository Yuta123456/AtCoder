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
        x ,y = que.popleft()
        if y*w+x not in finished:
            finished.add(y*w+x)
            for n_x,n_y in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if check(n_y,n_x) and graph[n_y][n_x] > graph[y][x] + 1:
                    graph[n_y][n_x] = graph[y][x] + 1
                    que.append((n_x,n_y))
for i in range(h):
    grid.append(list(input()))
que = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            graph[i][j] = 0
            que.append((j,i))
bfs(que)
ans = 0
for i in range(h):
    ans = max(ans, max(graph[i]))
print(ans)