from collections import deque
import math
n, d, a = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()
dam = 0
ans = 0
q = deque()
for i in range(n):
    x,h = data[i]
    while q:
        k = q.popleft()
        if k[1] >= x:
            q.appendleft(k)
            break
        else:
            dam -= k[0]
    h -= dam
    h = max(h, 0)
    count = math.ceil(h / a)
    dam += count * a
    q.append([count * a, x + 2*d])
    ans += count
print(ans)