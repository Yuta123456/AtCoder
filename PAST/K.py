def Euler_tour(node, depth):
    #終わりの頂点に追加
    finished.add(node)
    first_visit_id[node] = len(route_Euler)
    node_depth[node] = depth
    #隣接している頂点に対して操作を行う
    route_Euler.append(node)
    for i in adjacent_list[node]:
        if i not in finished:
            first_visit_id[node]
            Euler_tour(i, depth+1)
            route_Euler.append(node)
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

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
adjacent_list = tuple([] for i in range(n+1))
root = 0
for i in range(n):
    tmp = int(input())
    if tmp == -1:
        root = i+1
    else:
        adjacent_list[tmp].append(i+1)
finished = set()
route_Euler = []
node_depth = [0]*(n+1)
node_depth[0] = 10**5
first_visit_id = [0]*(n+1)
#オイラーツアー
Euler_tour(root, 0)
#seg木を初期化するやつ
init_array = [node_depth[i] for i in route_Euler]
ide_ele = 10**5
num =2**(len(init_array) - 1).bit_length()
seg=[ide_ele]*(2*num - 1)
init(init_array)
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    A = first_visit_id[a]
    B = first_visit_id[b]
    if query(min(A,B),max(A,B)) == node_depth[b]:
        print("Yes")
    else:
        print("No")