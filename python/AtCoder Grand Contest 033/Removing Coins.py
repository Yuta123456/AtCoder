from collections import deque
import sys
sys.setrecursionlimit(10**6)
n = int(input())
adjacent_list = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
dist = [0 for i in range(n+1)]
def bfs(node,pre_node):
    que = deque([(node, pre_node)])
    while que:
        node, pre_node = que.popleft()
        for i in adjacent_list[node]:
            if i != pre_node:
                dist[i] = dist[node] + 1
                que.append([i,node])
bfs(1,0)
index = dist.index(max(dist))
dist = [0 for i in range(n+1)]
bfs(index,0)
l = max(dist)
#一回の操作というのは,木の直径を1or2減らすことになる
if l % 3 == 1:
    print("Second")
else:
    print("First")