import copy
n,m,s = map(int, input().split())
adjacent_list = [[] for i in range(n+1)]
inf = 10**11
dist = [[inf for i in range(n+1)] for j in range(n+1)]
need_coin = [[inf for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    tmp = list(map(int, input().split()))
    adjacent_list[i].append(tmp)
    dist[tmp[0]][tmp[1]] = dist[tmp[1]][tmp[0]] = tmp[3]
    need_coin[tmp[0]][tmp[1]] = need_coin[tmp[1]][tmp[0]] = tmp[2]
translate = []
original = copy.deepcopy(dist)
for i in range(n):
    translate.append(list(map(int, input().split())))
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k] + dist[k][j])
def dijkstra_back(s,t,n,w,cost):
    #sからtへの最短経路の経路復元
    prev = [s] * n #最短経路の直前の頂点
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
        
        for i in range(n):
            if d[i] > d[v] + cost[v][i]: 
                d[i] = d[v] + cost[v][i]
                prev[i] = v
        
    path = [t]
    while prev[t] != s:
        path.append(prev[t])
        prev[t] = prev[prev[t]]
    path.append(s)
    path = path[::-1]
    return path

#print_ans
for i in range(2,n+1):
    print(dijkstra_back(1,i,n+1,m,original))