import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,u,v = map(int, input().split())
adjacent_list = [[] for i in range(n+1)]
aoki = [0 for i in range(n+1)]
takahashi = [0 for i in range(n+1)]
for i in range(n-1):
    a,b = map(int ,input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)

def dfs(node, count,li):
    global node_par
    li[node] = count
    finished.add(node)
    for i in adjacent_list[node]:
        if i not in finished:
            node_par[i] = node
            dfs(i, count + 1,li)
        
node_par = [0 for i in range(n+1)]

finished = set()
dfs(u,0,takahashi)

#辿って親保存しとく
finished = set()
dfs(v,0,aoki)

#さかのぼれるとこまで行く,startがさかのぼれる最大のノーど
par = u
start = u
while takahashi[par] < aoki[par]:
    start = par
    par = node_par[start]

ans_height = [0 for i in range(n+1)]
finished = set([node_par[start]])
dfs(start,0,ans_height)
print(max(ans_height) + aoki[start] - 1)
