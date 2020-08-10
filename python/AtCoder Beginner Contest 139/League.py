from collections import defaultdict
from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)
input = stdin.readline
n = int(input())
M = [[-1 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        M[i][j] = cnt
        M[j][i] = cnt
        cnt += 1
ans = 0
nodes = []
adjacent_list = [[] for i in range(n*(n-1)//2)]
for i in range(n):
    tmp = list(map(int, input().split()))
    pre = tmp[0] - 1
    nodes.append(M[i][pre])
    for j in tmp[1:]:
        adjacent_list[M[i][pre]].append(M[i][j-1])
        pre = j - 1
#まず、閉路検
seen = defaultdict(lambda: False)
visited = defaultdict(lambda: False)
def check(node):
    if visited[node]:
        return
    seen[node] = True
    for i in adjacent_list[node]:
        if seen[i] and (not visited[i]):
            print(-1)
            exit()
        check(i)
    visited[node] = True
def dfs_path(node):
    if depth[node]:
        return depth[node]
    tmp = 1
    for i in adjacent_list[node]:
        tmp = max(tmp, dfs_path(i) + 1)
    depth[node] = tmp
    return depth[node]
depth = [0 for i in range(n*(n-1)//2)]
for i in nodes:
    check(i)
    ans = max(ans, dfs_path(i))
print(ans)