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
        if (not check(x,y) ) or grid[y][x] == '#':
            continue
        if (x,y) not in finished:
            finished.add((x,y))
            graph[y][x] = cost
            que.append([x+1,y,cost+1])
            que.append([x, y+1, cost+1])
            que.append([x-1,y,cost+1])
            que.append([x,y-1,cost+1])