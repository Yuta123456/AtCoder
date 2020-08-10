from collections import deque
point = deque()
grid = []
r, c = list(map(int, input().split()))
sx,sy = list(map(int, input().split()))
gx, gy = list(map(int, input().split()))
for i in range(r):
    grid.append(list(input()))

def bfs():
    while len(point) != 0:
        x, y, count = point.popleft()
        if grid[x][y] != '#' and grid[x][y] == '.':

            grid[x][y] = count
            count += 1
            point.append([x, y + 1,count])
            point.append([x, y - 1,count])
            point.append([x + 1, y,count])
            point.append([x - 1, y,count])
point.append([sx - 1,sy - 1,0])
bfs()
print(grid[gx - 1][gy - 1])