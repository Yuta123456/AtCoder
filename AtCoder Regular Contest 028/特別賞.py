import heapq
n, k = map(int, input().split())
x = list(map(int, input().split()))
memo = dict()
for i in range(n):
    memo[x[i]] = i+1
priority_queue = list(map(lambda x: x*-1, x[:k]))
heapq.heapify(priority_queue)
for i in range(k,n):
    ans = heapq.heappop(priority_queue)
    print(memo[ans*-1])
    heapq.heappush(priority_queue,x[i]*-1)
    heapq.heappush(priority_queue,ans)
    heapq.heappop(priority_queue)
print(memo[heapq.heappop(priority_queue)*-1])
