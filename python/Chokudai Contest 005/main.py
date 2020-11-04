from collections import deque, defaultdict
import heapq
ID, n, k = map(int, input().split())
grid = []

for i in range(n):
    grid.append(list(input()))

def check(x,y):
    return ((0 <= x < n) and (0 <= y < n))
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]
par = [-1 for i in range(n*n)]
def p2n(x,y):
    return y*n + x

def print_grid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
# union find
for i in range(n):
    for j in range(n):
        for n_y, n_x in [(i + 1,j), (i, j + 1)]:
            if check(n_x, n_y) and grid[i][j] == grid[n_y][n_x]:
                unite(p2n(j,i), p2n(n_x,n_y))
value_of_point = []
heapq.heapify(value_of_point)
def bfs_valid(s_x, s_y):
    que = deque()
    que.append((s_x, s_y))
    count = defaultdict(int)
    cnt_fin = set()
    finished = set()
    while que:
        now_x, now_y = que.popleft()
        finished.add(p2n(now_x,now_y))
        for n_x, n_y in [(now_x + 1, now_y), (now_x,now_y + 1), (now_x-1, now_y),(now_x, now_y-1)]:
            if check(n_x, n_y) and (p2n(n_x, n_y) not in finished):
                if same(p2n(n_x,n_y), p2n(now_x,now_y)):
                    que.append((n_x,n_y))
                else:
                    if p2n(n_x,n_y) not in cnt_fin:
                        count[grid[n_y][n_x]] += 1
                        cnt_fin.add(p2n(n_x,n_y))
    if len(count) == 0:
        return 
    max_key = max(count, key=count.get)
    max_value = count[max_key]
    heapq.heappush(value_of_point, [-max_value,max_key,s_x,s_y])
def change_bfs(s_x, s_y, color):
    que = deque()
    que.append((s_x, s_y))
    finished = set()
    union_list = []
    while que:
        now_x, now_y = que.popleft()
        grid[now_y][now_x] = color
        finished.add(p2n(now_x,now_y))
        for n_x, n_y in [(now_x + 1, now_y), (now_x,now_y + 1), (now_x-1, now_y),(now_x, now_y-1)]:
            if check(n_x, n_y) and (p2n(n_x, n_y) not in finished):
                if same(p2n(n_x,n_y), p2n(now_x,now_y)):
                    que.append((n_x,n_y))
                if grid[n_y][n_x] == color:
                    union_list.append(p2n(n_x,n_y))
                    ignore_point.add(p2n(n_x,n_y))
    ori = p2n(s_x, s_y)
    for i in union_list:
        unite(ori,i)
    bfs_valid(s_x,s_y)
ans = []
for i in range(n):
    for j in range(n):
        bfs_valid(i, j)

ignore_point = set()

while value_of_point:
    print(len(value_of_point))
    point, new_num, x, y = heapq.heappop(value_of_point)
    if find(p2n(x,y)) not in ignore_point: 
        ans.append("{} {} {}".format(y+1,x+1,new_num))
        change_bfs(x,y,new_num)
for i in range(n):
    for j in range(n):
        bfs_valid(i, j)
while value_of_point:
    point, new_num, x, y = heapq.heappop(value_of_point)
    if find(p2n(x,y)) not in ignore_point: 
        ans.append("{} {} {}".format(y+1,x+1,new_num))
        change_bfs(x,y,new_num)

print_grid()
print(len(ans))
for i in ans:
    print(i)
