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