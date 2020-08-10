from collections import deque
q = deque()
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
total = 0
for i in range(n):
    total += a[i]
    q.append(a[i])
    if len(q) == k:
        ans += total
    if len(q) == k+1:
        p = q.popleft()
        total -= p
        ans += total
print(ans)