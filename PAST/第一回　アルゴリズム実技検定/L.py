from copy import deepcopy
from math import sqrt
n,m = map(int, input().split())
edge = []
big_tower = []
for i in range(n):
    x,y,c = map(int, input().split())
    for j in range(len(big_tower)):
        pre_x,pre_y,pre_c = big_tower[j]
        if pre_c == c:
            edge.append([i+1,j+1,sqrt(pow(x-pre_x,2) + pow(y-pre_y,2))])
        else:
            edge.append([i+1,j+1,sqrt(pow(x-pre_x,2) + pow(y-pre_y,2)) * 10])
    big_tower.append([x,y,c])
small_tower = []
for i in range(m):
    small_tower.append(list(map(int, input().split())))
ans = 10**18
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)
#xが属する集合の個数
def size(x):
    return -par[find(x)]

for i in range(pow(2,m)):
    copy_edge = deepcopy(edge)
    use_small_tower = []
    total_cost = 0
    #print(list("{:b}".format(i).zfill(m)))
    for index,flag in enumerate(list("{:b}".format(i).zfill(m))):
        if int(flag):
            x,y,c = small_tower[index]
            for pre_x,pre_y,pre_c,pre_i in use_small_tower:
                if pre_c == c:
                    copy_edge.append([n+1+index,pre_i,sqrt(pow(x-pre_x,2) + pow(y-pre_y,2))])
                else:
                    copy_edge.append([n+1+index,pre_i,sqrt(pow(x-pre_x,2) + pow(y-pre_y,2)) * 10])
            for j in range(n):
                pre_x,pre_y,pre_c = big_tower[j]
                if pre_c == c:
                    copy_edge.append([n+1+index,j+1,sqrt(pow(x-pre_x,2) + pow(y-pre_y,2))])
                else:
                    copy_edge.append([n+1+index,j+1,sqrt(pow(x-pre_x,2) + pow(y-pre_y,2)) * 10])
            use_small_tower.append([x,y,c,n+1+index])

    #いま、copy_edgeには試したい辺がすべて入っている状態
    par = [-1 for i in range(n+m+1)]
    copy_edge.sort(key=lambda x: x[2])
    #print("edge:",copy_edge)
    for node_1,node_2,cost in copy_edge:
        if not same(node_1,node_2):
            total_cost += cost
            unite(node_1,node_2)
    #print()
    #print("total : ",total_cost)
    #print("i:",i)
    ans = min(ans, total_cost)
print(ans)


