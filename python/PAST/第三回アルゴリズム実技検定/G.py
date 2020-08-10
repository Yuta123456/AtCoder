from collections import deque
n, X, Y = map(int, input().split())
grid = [['.' for j in range(450)] for j in range(450)]
for i in range(n):
    x,y = map(int, input().split())
    grid[y][x] = '#'
#x,y渡すと、（ｈ、ｗ）に入ってるかどうか判定
def check(s,t):
    if (-210 <= s <= 210) and (-210 <= t <= 200):
        return True
    else:
        return False
cost = [[10**5 for j in range(450)] for j in range(450)]
#graph => そこまでの距離を保存した二次元配列　grid=>与えられた迷路
def bfs():
    que = deque([])
    que.append((0,0))
    cost[0][0] = 0
    while que:
        x, y = que.popleft()
        for n_x, n_y in [(x+1,y+1), (x,y+1), (x-1,y+1),(x+1,y),(x-1, y), (x, y-1)]:
            if check(n_y, n_x) and grid[n_y][n_x] == '.' and cost[n_y][n_x] > cost[y][x] + 1:
                cost[n_y][n_x] = cost[y][x] + 1
                que.append((n_x,n_y))
bfs()
if cost[Y][X] == 10**5:
    print(-1)
else:
    print(cost[Y][X])