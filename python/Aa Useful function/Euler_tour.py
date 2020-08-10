finished = set()
route_Euler = []
node_depth = [0 for i in range(n+1)]
first_visit_id = [0 for i in range(n+1)]
def Euler_tour(node, depth):
    #終わりの頂点に追加
    finished.add(node)
    first_visit_id[node] = len(route_Euler)
    node_depth[node] = depth
    #隣接している頂点に対して操作を行う
    route_Euler.append(node)
    for i in adjacent_list[node]:
        if i not in finished:
            #first_visit_id[node]
            Euler_tour(i, depth+1)
            route_Euler.append(node)
#セグ木に乗せるときは、単位元に気を付けること