import sys
from collections import deque
sys.setrecursionlimit(10**7)
k = int(input())
ans = []
def bfs(que):
    finished = set()
    while que and len(ans) <= 10**5:
        x = que.popleft()
        ans.append(int(x))
        if x not in finished:
            finished.add(x)
            p = int(x[-1])
            if 1 <= p <= 8:
                que.append(x + str(p-1))
                que.append(x + str(p))
                que.append(x + str(p+1))
            elif p == 0:
                que.append(x + str(p))
                que.append(x + str(p+1))
            else:
                que.append(x + str(p-1))
                que.append(x + str(p))
que = deque([])
for i in range(1,10):
    que.append(str(i))
bfs(que)
ans.sort()
print(ans[k-1])