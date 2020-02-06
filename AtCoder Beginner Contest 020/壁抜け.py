from collections import deque
#x,y渡すと、（ｈ、ｗ）に入ってるかどうか判定
def check(s,t):
    if (0 <=  s <= w - 1) and (0 <= t <= h - 1):
        return True
    else:
        return False
#graph => そこまでの距離を保存した二次元配列　grid=>与えられた迷路
def bfs(sharp):
    inf = 10**14
    dist = [[inf for i in range(w)] for j in range(h)]
    que = deque()
    que.append([s_x,s_y,-1])
    while que:
        x , y, cost = que.popleft()
        if not check(x,y):
            continue
        if grid[y][x] == '#':
            cost += sharp
        else:
            cost += 1
        if dist[y][x] > cost:
            dist[y][x] = cost
            que.append([x+1,y,cost])
            que.append([x, y+1, cost])
            que.append([x-1,y,cost])
            que.append([x,y-1,cost])
    print(sharp)
    print(dist)
    print()
    if dist[g_y][g_x] <= t:
        return True
    else:
        return False

def binary_search(left, right):
    if right - left <= 1:
        return left
    middle = (right + left)//2
    if bfs(middle):
        return binary_search(middle, right)
    else:
        return binary_search(left, middle)
            
# -------------------------input----------------------
h, w, t = map(int, input().split())
grid = []
global s_x
global s_y
global g_x
global g_y
for i in range(h):
    grid.append(list(input()))
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'S':
            s_x = j
            s_y = i
        if grid[i][j] == 'G':
            g_x = j
            g_y = i
print(binary_search(-1,10**10))