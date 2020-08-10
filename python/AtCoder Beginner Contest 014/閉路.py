import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
adjacent_list = [[] for i in range(n+1)]
for i in range(n-1):
    x, y = map(int, input().split())
    adjacent_list[x].append(y)
    adjacent_list[y].append(x)
q = int(input())
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
Euler_tour(1,0)
#####segfunc######
def segfunc(x,y):
    return min(x,y)

def init(init_val):
    #set_val
    for i in range(len(init_val)):
        seg[i+num-1]=init_val[i]   
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res
n = len(route_Euler)
#####単位元######
ide_ele = 10**9
num =2**(n-1).bit_length()
seg=[ide_ele]*(2*num - 1)
init([node_depth[i] for i in route_Euler])
#阪堺区間に注意
for i in range(q):
    x,y = map(int, input().split())
    c,d = first_visit_id[x], first_visit_id[y]
    if c > d:
        c,d = d,c
    lca_depth = query(c, d+1)
    print(1 + node_depth[x] + node_depth[y] - lca_depth*2)
