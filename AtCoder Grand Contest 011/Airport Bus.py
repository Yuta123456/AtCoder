import bisect
import math
n, c, k = list(map(int, input().split()))
t = [0] * n
for i in range(n):
    t[i] = int(input())
t.sort()
t_max = t[-1]
t_min = t[0]
 
bus_count = 0
pre_index = 0
for i in range(t_min, t_max+1, k):
    index = bisect.bisect_right(t, i + k)
    if  pre_index != index:
        bus_count += math.ceil((index - pre_index) / c)
        pre_index = index
print(bus_count)
    