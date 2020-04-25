from collections import deque
n,m = map(int, input().split())
adjacent_list = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int, input().split())
    adjacent_list[u].append(v)
    adjacent_list[v].append(u)
ans = 0
close = 0
start_node = []
finished = set()

def dfs(node,parent):
    global flag
    finished.add(node)
    for i in adjacent_list[node]:
        if i not in finished:
            dfs(i,node)
        else:
            if i != parent:
                flag = True
for i in range(1,n+1):
    if i not in finished:
        dfs(i,0)
        start_node.append(i)
finished = set()
ans = len(start_node)
for i in start_node:
    flag = False
    dfs(i,0)
    if flag:
        ans -= 1
print(ans)