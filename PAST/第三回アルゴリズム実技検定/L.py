from heapq  import heappop, heappush,heapify
from collections import deque
n = int(input())
array = [[] for i in range(n)]
for i in range(n):
    t = deque(list(map(int, input().split())))
    t.popleft()
    array[i] = t
one = [[-array[i][0], i] for i in range(n)]
two = [[-array[i][0], i] for i in range(n)] + [[-array[i][1], i] for i in range(n)]
index_que = [-1 for i in range(n)]
heapify(one)
heapify(two)
finished = set()
m = int(input())
a = list(map(int, input().split()))
for i in range(m):
    if a[i] == 1:
        buy, index = heappop(one)
        while -buy in finished and len(one) > 0:
            buy, index = heappop(one)
        print(-buy)
        index_que[index] += 1
        finished.add(-buy)
        while len(array[index]) > 0 and index < index_que[index] + 1:
            heappush(one, [-array[index],index])
            index += 1

    else:
        buy, index = heappop(two)
        while -buy in finished and len(two) > 0:
            buy, index = heappop(two)
        print(-buy)
        index_que[index] += 1
        finished.add(-buy)
        tmp = index
        while len(array[index]) > 0 and index < index_que[index] + 1:
            heappush(one, [-array[index][index_que[index]],index])
        index = tmp
        while len(array[index]) > 0 and index < index_que[index] + 2:
            heappush(two, [-array[index],index])
            index += 1


