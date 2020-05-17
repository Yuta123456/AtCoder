import heapq
n = int(input())
ans = 0
can = []
heapq.heapify(can)
data = [[] for i in range(n+1)]
for i in range(n):
    a,b = map(int, input().split())
    data[a].append(b)
count = 0
ans = 0
for i in range(1,n+1):
    index = 0
    while index < len(data[i]):
        heapq.heappush(can, -data[i][index])
        index += 1
    ans += heapq.heappop(can) * (-1)
    print(ans)
