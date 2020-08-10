from collections import deque
n , m = map(int, input().split())
keys = deque()
def trans(k):
    res = [0 for i in range(n)]
    for i in k:
        res[-i] = 1
    res = int("".join(map(str, res)), 2)
    return res

for i in range(m):
    a, b = list(map(int, input().split()))
    c = deque(list(map(int, input().split())))
    c.appendleft(a)
    keys.append(c)
inf = 10 ** 8
dp = [inf for i in range(2**n)]
dp[0] = 0
for i in range(m):
    key_value = keys[i].popleft()
    can_open = keys[i]
    p = trans(can_open)
    for j in range(2**n):
        next = j | p
        dp[next] = min(dp[next], dp[j] + key_value)
#print(dp)
if dp[-1] >= inf:
    print(-1)
else:
    print(dp[-1])