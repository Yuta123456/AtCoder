from collections import deque 
n, m = map(int, input().split())
finished = set()
a = []
for i in range(m):
    a.append(int(input()))
a.reverse()
ans = []
for i in range(m):
    if a[i] not in finished:
        finished.add(a[i])
        ans.append(a[i])
for i in range(1,n+1):
    if i not in finished:
        ans.append(i)
for i in range(n):
    print(ans[i])


