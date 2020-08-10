import heapq
from collections import deque
import sys
input = sys.stdin.readline
x,y,a,b,c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort()
q.sort()
r.sort(reverse=True)
red_que = p[a-x:]
heapq.heapify(red_que)
green_que = q[b-y:]
heapq.heapify(green_que)
for i in range(c):
    re_mi = heapq.heappop(red_que)
    gr_mi = heapq.heappop(green_que)
    if re_mi < gr_mi:
        if re_mi < r[i]:
            heapq.heappush(red_que,r[i])
            heapq.heappush(green_que,gr_mi)
        else:
            heapq.heappush(green_que,gr_mi)
            heapq.heappush(red_que,re_mi)
            break
    else:
        if gr_mi < r[i]:
            heapq.heappush(red_que,re_mi)
            heapq.heappush(green_que,r[i])
        else:
            heapq.heappush(green_que,gr_mi)
            heapq.heappush(red_que,re_mi)
            break
print(sum(green_que) + sum(red_que))