import sys
sys.setrecursionlimit(10**6)
n = int(input())
tree = [[] for i in range(n + 1)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    tree[u].append([v,w])
    tree[v].append([u,w])
finished = set()
ans = [-1 for i in range(n + 1)]
def dfs(node, weight):
    finished.add(node)
    if weight % 2 == 0:
        ans[node] = 0
    else:
        ans[node] = 1
    for i in tree[node]:
        next, w = i
        if next not in finished:
            dfs(next, w + weight)
dfs(1,0)
for i in range(1, len(ans)):
    print(ans[i])