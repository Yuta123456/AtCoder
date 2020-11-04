from collections import deque

h , w = map(int, input().split())
start_y, start_x = map(int, input().split())
end_y, end_x = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
cost = [[float('inf') for i in range(w)] for j in range(h)]

def bfs():
    que = deque()
    que.append((start_x-1, start_y-1,0))
    que_contents = set()
    while que:
        x, y, c = que.popleft()
        if not ((0 <= y < h) and (0 <= x < w)) :
            continue
        if grid[y][x] == '#':
            continue
        if cost[y][x] <= c:
            continue
        cost[y][x] = c
        for n_x, n_y in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if (n_x,n_y) not in que_contents:
                que.appendleft((n_x, n_y, c))
                finished.add((n_x, n_y))
        for i in range(-2,3):
            for j in range(-2,3):
                if (x+i,y+j) not in finished:
                    que.append((x+i,y+j,c+1))
bfs()
if cost[end_y-1][end_x-1] == float('inf'):
    print(-1)
    exit()
print(cost[end_y-1][end_x-1])
