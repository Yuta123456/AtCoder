import heapq
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [i * (-1) for i in a]
heapq.heapify(a)
b.sort(reverse=True)
for i in range(m):
    if len(a) != 0:
        k  = heapq.heappop(a) * (-1)
    else:
        print("NO")
        exit()
    if k < b[i]:
        print("NO")
        exit()
print("YES")
