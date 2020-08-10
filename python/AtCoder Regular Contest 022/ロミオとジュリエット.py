import sys
sys.setrecursionlimit(10**6)
n = int(input())
adjacent_list = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
def dfs(node, c):
    finished.add(node)
    dist[node] = c
    for i in adjacent_list[node]:
        if i not in finished:
            dfs(i, c+1)
dist = [0 for i in range(n+1)]
finished = set()
dfs(1,0)
max_dist = -1
max_node = -1
for i in range(1,n+1):
    if max_dist < dist[i]:
        max_dist = dist[i]
        max_node = i
dist = [0 for i in range(n+1)]
finished = set()
dfs(max_node, 0)
ans_dist = 0
ans_node = 0
for i in range(1,n+1):
    if ans_dist < dist[i]:
        ans_dist = dist[i]
        ans_node = i
print("{} {}".format(ans_node, max_node))
