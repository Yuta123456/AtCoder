import sys
sys.setrecursionlimit(10**6)
h,w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
#色が変わるところでコスト
inf = 10**9
#x,y渡すと、（ｈ、ｗ）に入ってるかどうか判定
#graph => そこまでの距離を保存した二次元配列　grid=>与えられた迷路
adjacent_list = [[] for i in range(h*w+1)]
for i in range(h):
    for j in range(w):
        if i == (h-1) and j == (w-1):
            continue
        if j != (w-1):
            if grid[i][j] != grid[i][j+1] and grid[i][j] == '#':
                adjacent_list[w*i + (j + 1)].append([w*(i) + (j + 2), 1])
            else:
                adjacent_list[w*i + (j + 1)].append([w*(i) + (j + 2), 0])
        if i != (h-1):
            if grid[i][j] != grid[i+1][j] and grid[i][j] == '#':
                adjacent_list[w*i + (j + 1)].append([w*(i + 1) + (j + 1), 1])
            else:
                adjacent_list[w*i + (j + 1)].append([w*(i + 1) + (j + 1), 0])
finished = set()
def dfs(node,cost):
    finished.add(node)
    for i in adjacent_list[node]:
        if dist[node] + i[1] < dist[i[0]]:
            dist[i[0]] = dist[node] + i[1]
            dfs(i[0],i[1])
dist = [inf for i in range(h*w+1)]
dist[1] = 0
dfs(1,0)
if grid[-1][-1] == '#':
    dist[-1] += 1
print(dist[-1])

