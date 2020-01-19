from collections import deque
h,w = map(int, input().split())
inf = 10**2
graph = []
for i in range(h):
    graph.append(list(map(int, input().split())))
que = deque()
que.append([h-1,0])
cost = [[inf for i in range(w)] for j in range(h)]
cost[h-1][0] = 0
#cost[h-1][w-1] = 0
def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False

def bfs(cost):
    while que:
        x, y  = que.popleft()
        cur_cost = cost[x][y]
        if check(x+1,y):
            if cur_cost + graph[x+1][y] < cost[x+1][y]:
                cost[x+1][y] = cur_cost + graph[x+1][y]
                que.append([x+1, y])
        if check(x,y+1):
            if cur_cost + graph[x][y+1] < cost[x][y+1]:
                cost[x][y+1] = cur_cost + graph[x][y+1]
                que.append([x, y+1])
        if check(x-1, y):
            if cur_cost + graph[x-1][y] < cost[x-1][y]:
                cost[x-1][y] = cur_cost + graph[x-1][y]
                que.append([x-1, y])
        if check(x, y-1):
            if cur_cost + graph[x][y-1] < cost[x][y-1]:
                cost[x][y-1] = cur_cost + graph[x][y-1]
                que.append([x, y-1])
    return cost
cost = bfs(cost)
for i in range(h):
    print(cost[i])  
