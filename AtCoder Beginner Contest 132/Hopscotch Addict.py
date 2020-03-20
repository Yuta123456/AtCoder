from collections import deque
n, m = map(int, input().split())
inf = 10**9
def bfs(start):
    dist = [inf for i in range((n+1) * 3)]
    que = deque()
    que.append(start)
    finished = set()
    dist[start] = 0
    while que:
        node = que.popleft()
        if node not in finished:
            finished.add(node)
            for i in adjacent_list[node]:
                dist[i] = min(dist[i], dist[node] + 1)
                que.append(i)
    return dist

adjacent_list = [[] for i in range((n+1)*3)]
for _ in range(m):
    u, v = map(int, input().split())
    for i in range(3):
        adjacent_list[u*3 + i].append(v*3 +((i+1)%3))
start, goal = map(int, input().split())
graph = bfs(start*3)
if graph[goal*3] != inf:
    print(int(graph[goal*3]) // 3)
else:
    print(-1)