from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
adjacent_list = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
ans = [-1 for i in range(n+1)]
def bfs():
    #start at 1
    que = deque([1])
    finished = set()
    while que:
        node = que.popleft()
        finished.add(node)
        print(node)
        for i in adjacent_list[node]:
            if i not in finished:
                que.append(i)
                if ans[i] == -1:
                    ans[i] = node
bfs()
print("Yes")
for i in range(2,n+1):
    print(ans[i])
