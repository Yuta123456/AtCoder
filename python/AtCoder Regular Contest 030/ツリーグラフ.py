n,x = map(int, input().split())
h = list(map(int, input().split()))
h = set([i + 1 for i in range(n) if h[i] == 1])
finished = set()
route_Euler = []
first_visit_id = [0 for i in range(n+1)]
last_visit_id = [0 for i in range(n+1)]
def Euler_tour(node):
    #終わりの頂点に追加
    finished.add(node)
    first_visit_id[node] = len(route_Euler)
    #隣接している頂点に対して操作を行う
    route_Euler.append(node)
    for i in adjacent_list[node]:
        if i not in finished:
            #first_visit_id[node]
            Euler_tour(i)
            route_Euler.append(node)
    last_visit_id[node] = len(route_Euler)-1
adjacent_list = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
Euler_tour(x)
finished = set()
def nessesary(node):
    part_tree = route_Euler[first_visit_id[node]:last_visit_id[node]+1]
    flag = False
    #print("node: {}, part :{}".format(node, part_tree))
    for i in part_tree:
        if i in h:
            flag = True
    return flag
def calc(node):
    global ans
    finished.add(node)
    for i in adjacent_list[node]:
        if i not in finished and nessesary(i):
            ans += 2
            calc(i)
ans = 0
calc(x)
print(ans)


