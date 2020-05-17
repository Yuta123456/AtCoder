def Euler_tour(node,depth):
    tank = [node]
    #多分ゼロ
    eulerNum = 0
    while tank:
        q = tank.pop()
        if q >= 0:
            #first time
            eulerNum += 1
            route_Euler.append(q)
            first_visit_id[q] = eulerNum
            tank.append(~q)
            depth += 1
            node_depth[q] = depth #深さ
            for ch in child[q]:
                tank.append(ch)
        else: #すべての頂点は必ず2度通るので、ifで引っかからなければ帰り道
            depth -= 1
            if ~q != root: #ビット反転(反転を反転)したものが根である場合は既に処理済みなので飛ばす
                route_Euler.append(*parent[~q]) #親=bit反転したもの
                eulerNum += 1 #オイラー路の順番
#####segfunc######
def init(init_val):
    #set_val
    for i in range(len(init_val)):
        seg[i+num-1]=init_val[i]   
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=min(seg[2*i+1],seg[2*i+2])
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = min(res,seg[p])
        if q&1 == 1:
            res = min(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res,seg[p])
    else:
        res = min(min(res,seg[p]),seg[q])
    return res

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
child = tuple([] for i in range(n+1))
parent = tuple([] for i in range(n+1))
root = 0
for i in range(n):
    tmp = int(input())
    if tmp == -1:
        root = i+1
    else:
        child[tmp].append(i+1)
        parent[i+1].append(tmp)
finished = set()
route_Euler = []
node_depth = [0]*(n+1)
node_depth[0] = 10**6
first_visit_id = [0]*(n+1)
#オイラーツアー
Euler_tour(root, 0)
#seg木を初期化するやつ
init_array = [node_depth[i] for i in route_Euler]
#print("init array",init_array)
ide_ele = 10**6
num =2**(len(init_array) - 1).bit_length()
seg=[ide_ele]*(2*num - 1)
init(init_array)
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    A = first_visit_id[a]-1
    B = first_visit_id[b]-1
    #print("{} {}".format(A,B))
    if query(min(A,B),max(A,B)) == node_depth[b]:
        print("Yes")
    else:
        print("No")