def Euler_tour(node, depth):
    #終わりの頂点に追加
    finished.add(node)
    first_visit_id[node] = len(route_Euler)
    node_depth[node] = depth
    #隣接している頂点に対して操作を行う
    route_Euler.append(node)
    for i in adjacent_list[node]:
        if i not in finished:
            Euler_tour(i, depth+1)
            route_Euler.append(node)

def calc_dis(node, dis,li):
    finished = set()
    stack = deque()
    stack.append([node, dis])
    while stack:
        node, dis = stack.pop()
        li[node] = dis
        finished.add(node)
        for i in adjacent_list[node]:
            if i not in finished:
                stack.append([i, dis+1])
from collections import deque
n, u, v = map(int, input().split())
adjacent_list = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
inf = 10**6
takahashi_to_v = [inf for _ in range(n+1)]
aoki_to_v = [inf for _ in range(n+1)]
#二人の最短距離を求めるために、オイラーツアーを使う。
#LCAを求め、そこを経由するようにする。aoki -> LCA -> takahashiが最短経路
#最短経路を求めた後は、ギリギリいけるところまで行ってから、そこから一番遠い頂点に向かう
finished = set()
route_Euler = []
node_depth = [0 for i in range(n+1)]
first_visit_id = [0 for i in range(n+1)]
#1を根として、オイラーツアーをする。
Euler_tour(1,1)
#LCAを求める。
lca = inf
for i in range(min(first_visit_id[u], first_visit_id[v]), max(first_visit_id[u], first_visit_id[v])):
    lca = min(lca, node_depth[route_Euler[i]])
calc_dis(u,0,takahashi_to_v)
calc_dis(v,0,aoki_to_v)