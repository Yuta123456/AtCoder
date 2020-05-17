from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
edge = []
ans = []
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
par = [-1]*(n+1)
for i in range(m):
    edge.append(list(map(int, input().split())))
edge.sort(key=lambda x: x[2])
q = int(input())
query = []
for i in range(q):
    query.append([i] + list(map(int, input().split())))
query.sort(key=lambda x: x[2])
query = deque(query)
edge = deque(edge)
for i in range(q):
    index, node, person_year = query.pop()
    while edge and edge[-1][2] > person_year:
        a,b,edge_year = edge.pop()
        unite(a,b)
    ans.append([index, size(node)])
ans.sort()
for i in range(q):
    print(ans[i][1])

