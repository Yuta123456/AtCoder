import heapq
n,k = map(int, input().split())
machine = []
for i in range(n):
    machine.append(list(map(int, input().split())))
heapq.heapify(machine)
ans = 0
for i in range(k):
    fastest = heapq.heappop(machine)
    ans += fastest[0]
    fastest[0] += fastest[1]
    heapq.heappush(machine, fastest)
print(ans)