import heapq
from collections import defaultdict
n, m = list(map(int, input().split()))

#list型のdistを初期化 works[key]:{list}になっている
works = defaultdict(list)
for i in range(n):
    a, b = list(map(int, input().split()))
    #a日後にお金が振り込まれる物のlistを作成
    works[a].append(b)
candidate = []
ans = 0
heapq.heapify(candidate)
for i in range(1,m+1):
    for j in works[i]:
        heapq.heappush(candidate, -j)
    if len(candidate) != 0:
        ans += heapq.heappop(candidate)

print(-ans)
