import heapq
n, m = map(int, input().split())
A = list(map(int, input().split()))
cost = []
heapq.heapify(cost)
for i in range(n):
    heapq.heappush(cost, -A[i])
for i in range(m):
    target = heapq.heappop(cost) / 2
    heapq.heappush(cost, target)
ans = [int(i) for i in cost]
print(-sum(ans))
