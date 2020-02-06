from collections import deque
import math
import bisect
n, d, a = map(int, input().split())
data = []
x_point = []
for i in range(n):
    x,h = map(int, input().split())
    data.append([x,h])
    x_point.append(x)
data.sort()
x_point.sort()
imos = [0] * (n+2)
ans = 0
for i in range(1,n+1):
    x, h = data[i-1]
    imos[i] += imos[i-1]
    index = bisect.bisect_right(x_point, x + 2*d)
    h -= imos[i]
    count = max(math.ceil(h/a), 0)
    ans += count
    imos[i] += count*a
    if index + 1 <= n:
        imos[index+1] -=count*a
print(ans)

