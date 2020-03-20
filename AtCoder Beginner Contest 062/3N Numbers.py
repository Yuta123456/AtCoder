import heapq
import bisect
n = int(input())
a = list(map(int, input().split()))
first_que = [a[i] for i in range(n)]
first_sum = sum(first_que)
heapq.heapify(first_que)
latter_que = [a[i] * -1 for i in range(2*n,3*n)]
latter_sum = sum(latter_que) * -1
heapq.heapify(latter_que)
ans = [0 for i in range(n+1)]
ans[0] = first_sum
for i in range(n,2*n):
    heapq.heappush(first_que, a[i])
    p = heapq.heappop(first_que)
    first_sum += (a[i] - p)
    ans[i-n+1] = first_sum
ans[-1] -= latter_sum

for i in range(2*n-1,n-1,-1):
    heapq.heappush(latter_que,a[i]*(-1))
    p = heapq.heappop(latter_que) * (-1)
    latter_sum += (a[i] - p)
    ans[i-n] -= latter_sum
print(max(ans))


